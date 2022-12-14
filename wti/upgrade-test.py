#!/usr/bin/env python3

import json
import os
import tempfile
import shutil
import sys
import getopt

try:
    import requests
except ImportError:
    print("The 'requests' modules is required for this code.")
    exit(1)

try:
    import urllib3
except ImportError:
    print("The 'urllib3' modules is required for this code.")
    exit(1)

# supress Unverified HTTPS request, only do this in a verified environment
urllib3.disable_warnings()

# Address of the WTI device
URI = "https://"
SITE_NAME = "172.20.3.94"

# put in the username and password to your WTI device here
USERNAME = "super"
PASSWORD = "super"

usersuppliedfilename = None
localfilefamily = -1
result = ""
forceupgrade = 0
family = 1
fips = None
checkonly = 0
parameterspassed = 0

assert sys.version_info >= (3, 0)

print("WTI Device Upgrade Program 1.0 (Python)\n")

try:
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, 'hm:f:l:a:n:p:c:', ["mode=", "file=", "layer=", "address=", "name=", "pass=", "checkonly="])

    for opt, arg in opts:
        if opt == '-h':
            print ('upgrade.py --file <localimagefilename> --layer <http:// https://> --address <address of device> --name <username> --pass <password> --checkonly yes --mode force')
            exit(0)
        elif opt in ("-m", "--mode"):
            if (arg == "force"):
                forceupgrade = 1
            parameterspassed = (parameterspassed | 1)
        elif opt in ("-f", "--file"):
            usersuppliedfilename = arg
            parameterspassed = (parameterspassed | 2)
        elif opt in ("-l", "--layer"):
            URI = arg
            parameterspassed = (parameterspassed | 4)
        elif opt in ("-a", "--address"):
            SITE_NAME = arg
            parameterspassed = (parameterspassed | 8)
        elif opt in ("-n", "--name"):
            USERNAME = arg
            parameterspassed = (parameterspassed | 16)
        elif opt in ("-p", "--pass"):
            PASSWORD = arg
            parameterspassed = (parameterspassed | 32)
        elif opt in ("-c", "--checkonly"):
            if ((arg.upper() == "YES") or (arg.upper() == "Y")):
                checkonly = 1
            parameterspassed = (parameterspassed | 64)

except getopt.GetoptError:
    print ('upgrade.py --file <localimagefilename> --layer <http:// https://> --address <address of device> --name <username> --pass <password> --checkonly yes --mode force')
    exit(2)

# if a local file was defined lets see what family it is: Console or Power
if (usersuppliedfilename is not None):
    try:
        ifilesize = os.path.getsize(usersuppliedfilename)
        file = open(usersuppliedfilename, 'rb')
        file.seek(ifilesize-20)
        fileread = file.read()
        if (fileread.find(b'TSM') >= 0):
            localfilefamily = 1
        elif (fileread.find(b'VMR') >= 0):
            localfilefamily = 0
        file.close()
        print("User Supplied file [%s] is a %s type." % (usersuppliedfilename, ("Console" if localfilefamily == 1 else "Power")))
    except Exception as ex:
        print("User Supplied file [%s] does not exist\n\n" % (usersuppliedfilename))
        print(ex)
        exit(1)

if ((parameterspassed & 4) == 0):
    tempdata = input("Enter Protocol [default: %s ]: " % (URI))
    if (len(tempdata) > 0):
        URI = tempdata

if ((parameterspassed & 8) == 0):
    tempdata = input("Enter Device Address [default: %s ]: " % (SITE_NAME))
    if (len(tempdata) > 0):
        SITE_NAME = tempdata

if ((parameterspassed & 16) == 0):
    tempdata = input("Enter Device Username [default: %s ]: " % (USERNAME))
    if (len(tempdata) > 0):
        USERNAME = tempdata

if ((parameterspassed & 32) == 0):
    tempdata = input("Enter Device Password [default: %s ]: " % (PASSWORD))
    if (len(tempdata) > 0):
        PASSWORD = tempdata

if ((parameterspassed & 64) == 0):
    tempdata = input("Check Only [default: %s ]: " % ("No"))
    if (len(tempdata) > 0):
        if ((tempdata.upper() == "YES") or (tempdata.upper() == "Y")):
            checkonly = 1

try:
    # 1. Get the current version and the device type of a WTI device
    fullurl = ("%s%s/cgi-bin/getfile" % (URI, SITE_NAME))

    print("\nChecking version and type of WTI device at: %s%s" % (URI, SITE_NAME))

    response = requests.get(URI+SITE_NAME+"/api/v2/status/firmware", auth=(USERNAME, PASSWORD), verify=False)
    if (response.status_code == 200):
        result = response.json()

        statuscode = result["status"]["code"]
        if (int(statuscode) != 0):
            exit(1)

#		Uncomment to see the JSON return by the unit
#        print(response.text)
        local_release_version = result["config"]["firmware"]
        try:
            family = int(result["config"]["family"])
        except Exception as ex:
            family = 1

        try:
            fips = result["config"]["fips"]
            if (fips == 0):
                fips = 1  # MAKE 2, 1 ONLY TEST: get me the no fips or merged code
        except Exception as ex:
            fips = 1

        print("Device reports Version: %s, Family: %s\n" % (local_release_version, ("Console" if family == 1 else "Power")))
        if (localfilefamily != -1):
            if (family != localfilefamily):
                print("FAMILY MISMATCH: Your local file is a %s type, and the device is a %s type\n\n" % (("Console" if localfilefamily == 1 else "Power"), ("Console" if family == 1 else "Power")))
                exit(3)

    else:
        if (response.status_code == 404):
            # lets see its its an older PPC unit
            response = requests.get(URI+SITE_NAME+"/cgi-bin/gethtml?formWTIProductStatus.html", auth=(USERNAME, PASSWORD), verify=False)
            if (response.status_code == 200):
                result = response.text.find('PPC / ')
                if (result >= 0):
                    print("\n[%s] is a PPC type unit. These units are EOL and do not support the RESTFUL API command set." % (SITE_NAME))
                    exit(4)

        print("Error Step 1: %s\n" % (response.status_code))
        exit(5)

    # 2. Go online and find the latest version of software for this WTI device if there was not local file defined
    if (localfilefamily == -1):
        fullurl = ("https://my.wti.com/update/version.aspx?fam=%s" % (family))
        if (fips is not None):
            fullurl = ("%s&fipsonly=%d" % (fullurl, int(fips)))

        print("Checking WTI for the latest OS version for a %s unit\n" % (("Console" if family == 1 else "Power")))

        response = requests.get(fullurl)
        if (response.status_code == 200):
            result = response.json()
        else:
            print("Error Step 1: %s\n" % (response.status_code))
            exit(6)

        remote_release_version = result["config"]["firmware"]

        if ((float(local_release_version) < 6.58) & (family == 1)) | ((float(remote_release_version) < 2.15) & (family == 0)):
            print("Error: WTI Device does not support remote upgrade\n")
            exit(7)

        print("WTI reports the latest of a %s is Version: %s\n" % (("Console" if family == 1 else "Power"), remote_release_version))
        statuscode = result['status']["code"]
    else:
        remote_release_version = 0

    if (int(statuscode) == 0):
        local_filename = None
        if ((float(local_release_version) < float(remote_release_version)) or (forceupgrade == 1)) or (localfilefamily >= 0):
            if (checkonly == 0):
                if (localfilefamily == -1):
                    online_file_location = result["config"]["imageurl"]

                    local_filename = online_file_location[online_file_location.rfind("/")+1:]
                    local_filename = tempfile.gettempdir() + "/" + local_filename

                    print("Downloading %s --> %s\n" % (online_file_location, local_filename))

                    response = requests.get(online_file_location, stream=True)
                    handle = open(local_filename, "wb")
                    for chunk in response.iter_content(chunk_size=512):
                        if chunk:  # filter out keep-alive new chunks
                            handle.write(chunk)
                    handle.close()
                else:
                    if (family == localfilefamily):
                        local_filename = usersuppliedfilename
                    else:
                        print("FAMILY MISMATCH: Your local file is a %s type, and the device is a %s type\n\n" % (("Console" if localfilefamily == 1 else "Power"), ("Console" if family == 1 else "Power")))
                        exit(3)
                # SEND the file to the WTI device
                fullurl = ("%s%s/cgi-bin/getfile" % (URI, SITE_NAME))
                files = {'file': ('name.binary', open(local_filename, 'rb'), 'application/octet-stream')}

                print("Sending %s --> %s%s\n" % (local_filename, URI, SITE_NAME))

                response = requests.post(fullurl, files=files, auth=(USERNAME, PASSWORD), verify=False, stream=True)
                result = response.json()

                print("response: %s\n" % (response))
                print(response.text)

                if (response.status_code == 200):
                    parsed_json = response.json()
                    if (int(parsed_json['status']["code"]) == 0):
                        print("\n\nUpgrade Successful, please wait a few moments while [%s] processes the file.\n" % (SITE_NAME))
                    else:
                        print("\n\nUpgrade Failed for [%s].\n" % (SITE_NAME))

                # only remove if the file was downloaded
                if (localfilefamily == -1):
                    os.remove(local_filename)
            else:
                if (localfilefamily == -1):
                    print("Device at [%s] is out of date.\n" % (SITE_NAME))
        else:
            print("Device at [%s] is up to date.\n" % (SITE_NAME))

    else:
        print("Error: %s\n" % (response.status_code))

except requests.exceptions.RequestException as e:
    print (e)
