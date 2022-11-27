# Jeff Comer
# script to upload apic and switch firmware and upgrade apic sw

import urllib.request
import urllib3
import sys, time
import getopt
import requests
import csv, json, pprint
import random
from random import seed
from aciOps import bakeCookies

def apicUpgrade(specDict, cookie):
    jsonPayload = ""
    payloadURL = ""
    bakeTimer = 0

    with open(specDict['file'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        switchInventoryDict = list(csvread)
    baseURL = "https://" + specDict['hostIp']
    tokenURL = baseURL + "/api/aaaLogin.json"

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    controllerFwPol = baseURL + "/api/node/class/firmwareCtrlrFwP.json"
    uploadHeader = {"content-type": "application/json"}
    for i in range(len(switchInventoryDict)):
        if(switchInventoryDict[i]['imageURL'] != ""):
            random.seed()
            r_number = random.randint(0, 2000)
            uploadName = "apic-" + str(r_number)
            uploadDn = "uni/fabric/fwrepop/osrc-" + uploadName
            if ("apic" in switchInventoryDict[i]['aciSoftware']):
                apicSwDn = uploadDn
                apicStatusURL = baseURL + "/api/node/mo/fwrepo/download-" + uploadName + ".json"
            elif ("n9000" in switchInventoryDict[i]['aciSoftware']):
                switchSwDn = uploadDn
                switchStatusURL = baseURL + "/api/node/mo/fwrepo/download-" + uploadName + ".json"
            uploadURL = baseURL + "/api/node/mo/uni/fabric/fwrepop/osrc-" + uploadName + ".json"
            uploadPayload = {"firmwareOSource":{"attributes":{"dn":uploadDn,"name":uploadName,"proto":"http","url":switchInventoryDict[i]['imageURL'],"status":"created,modified","rn":"osrc-apicSoftware"},"children":[]}}
            uploadResult = requests.post(uploadURL, json=uploadPayload, cookies=cookie, verify=False)

    time.sleep(120)
    
    for statusCheck in range(0, 400):
        switchUploadStatus = requests.get(switchStatusURL, cookies=cookie, verify=False)
        statusJson = switchUploadStatus.json()
        currentState = statusJson["imdata"][0]["firmwareDownload"]["attributes"]["dnldPercent"]
        print("Current Download %: " + currentState)
        if (int(currentState) == 100):
            statusCheck = 500
            bakeTimer = 0
            break
        elif (int(currentState) != 100):
            statusCheck += 1
            bakeTimer += 1
            pprint.pprint(switchUploadStatus.text)
            time.sleep(5)
            if (bakeTimer == 30):
                cookie = bakeCookies(specDict)
                bakeTimer = 0

    tokenHeader = {"content-type": "application/json"}
    jsonPayload = {'aaaUser':{"attributes":{'name':specDict['username'],'pwd':specDict['password']}}}
    tokenResponse = requests.post(tokenURL, json=jsonPayload, verify=False)
    jsonData = tokenResponse.json()
    token = jsonData["imdata"][0]["aaaLogin"]["attributes"]["token"]
    cookie = {'APIC-cookie':token}

    for statusCheck in range(0, 400):
        apicUploadStatus = requests.get(apicStatusURL, cookies=cookie, verify=False)
        statusJson = apicUploadStatus.json()
        currentState = statusJson["imdata"][0]["firmwareDownload"]["attributes"]["dnldPercent"]
        print("Current Download %: " + currentState)
        if (int(currentState) == 100):
            statusCheck = 500
            bakeTimer = 0
            break
        elif (int(currentState) != 100):
            statusCheck += 1
            pprint.pprint(apicUploadStatus.text)
            time.sleep(5)
            bakeTimer += 1
            if (bakeTimer == 30):
                cookie = bakeCookies(specDict)
                bakeTimer = 0

    time.sleep(60)
    apicUpgradeURL = baseURL + "/api/node/mo/uni/controller.json"
    for i in range(len(switchInventoryDict)):
        if("apic" in switchInventoryDict[i]['aciSoftware']):
            apicUpgradeVersion = switchInventoryDict[i]['aciSoftware']
            print(apicUpgradeVersion)

    apicUpgradePayload = {"ctrlrInst":{"attributes":{"dn":"uni/controller","status":"modified"},"children":[{"firmwareCtrlrFwP":{"attributes":{"dn":"uni/controller/ctrlrfwpol","version":apicUpgradeVersion,"ignoreCompat":"true"},"children":[]}},{"maintCtrlrMaintP":{"attributes":{"dn":"uni/controller/ctrlrmaintpol","adminSt":"triggered","adminState":"up"},"children":[]}},{"trigSchedP":{"attributes":{"dn":"uni/controller/schedp-ConstSchedP","status":"modified"},"children":[{"trigAbsWindowP":{"attributes":{"dn":"uni/controller/schedp-ConstSchedP/abswinp-ConstAbsWindowP"},"children":[]}}]}}]}}
    apicUpgradeResult = requests.post(apicUpgradeURL, json=apicUpgradePayload, cookies=cookie, verify=False)
    upgradeCheckURL = baseURL + "/api/node/mo/topology/pod-1/node-1/sys/ctrlrfwstatuscont/upgjob.json"
    time.sleep(120)
    cookie = bakeCookies(specDict)

    for upgradeCheck in range(0, 800):
        print("Bake Count: " + str(bakeTimer))
        if bakeTimer >= 30:
            try:
                cookie = bakeCookies(specDict)
                bakeTimer = 0
            except:
                time.sleep(30)
        try:
            upgradeStatus = requests.get(upgradeCheckURL, cookies=cookie, verify=False)
            upgradeJson = upgradeStatus.json()
            print(upgradeJson)
            try:
                upgradeResult = upgradeJson["imdata"][0]["maintUpgJob"]["attributes"]["upgradeStatusStr"]
                if (upgradeResult == "Successful"):
                    upgradeCheck = 900
                    bakeTimer = 0
                    print(upgradeResult)
                    break
                elif (upgradeResult != "Successful"):
                    upgradeCheck += 1
                    bakeTimer += 1
                    #pprint.pprint(upgradeStatus.text)
                    print(upgradeResult)
                if (upgradeCheck == 800):
                    print("Upgrade timeout Expired.  Please verify status via APIC")
                    exit(-1)
                time.sleep(5)
                if (bakeTimer == 30):
                    cookie = bakeCookies(specDict)
                    bakeTimer = 0
            except:
                upgradeCheck += 1
                bakeTimer += 1
                time.sleep(5)
                if (bakeTimer == 30):
                    cookie = bakeCookies(specDict)
                    bakeTimer = 0
                print("Looking for valid json response")
            
        except requests.exceptions.Timeout:
            print("Retrying Connection, Node Reset")
            upgradeCheck += 1
            bakeTimer += 1
            time.sleep(30)
        except requests.exceptions.ConnectionError:
            print("Retrying Connection, Connection Refused")
            upgradeCheck += 1
            bakeTimer += 1
            time.sleep(60)




def main(argv):
    """
    Main execution routine

    :return: None
    """

    username = ""
    password = ""
    hostIp = ""
    userArg = ""
    pwArg = ""
    hostIpArg = ""

    argDict = {"username":"","password":"","hostIp":"","file":""}
    try:
      opts, args = getopt.getopt(argv,"hu:p:i:f:",["username","password","hostIp=","file="])
    except getopt.GetoptError:
      print('apicUpgrade.py -u <username> -p <password> -i <host_ip> -f <inputfile>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('apicUpgrade.py -u <username> -p <password> -i <host_ip> -f <inputfile>')
         sys.exit()
      elif opt in ("-u", "--username"):
         userArg = arg
         argDict["username"] = userArg
      elif opt in ("-p", "--password"):
         pwArg = arg
         argDict["password"] = pwArg
      elif opt in ("-i", "--hostIp"):
         hostIpArg = arg
         argDict["hostIp"] = hostIpArg
      elif opt in ("-f", "--file"):
         file = arg
         argDict["file"] = file
    return argDict

if __name__ == '__main__':
    cliArgs = main(sys.argv[1:])
    apicSnacks = bakeCookies(cliArgs)
    apicUpgradeResult = apicUpgrade(cliArgs, apicSnacks)
    