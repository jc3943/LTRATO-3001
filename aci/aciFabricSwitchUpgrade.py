# Jeff Comer
# script to upload apic and switch firmware and upgrade an apic

import urllib.request
import urllib3
import sys, time
import getopt
import requests
import csv, json, pprint
import random
from random import seed

def apicUpgrade(specDict):
    jsonPayload = ""
    payloadURL = ""

    with open(specDict['file'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        switchInventoryDict = list(csvread)
    baseURL = "https://" + specDict['hostIp']
    tokenURL = baseURL + "/api/aaaLogin.json"

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    tokenHeader = {"content-type": "application/json"}
    jsonPayload = {'aaaUser':{"attributes":{'name':specDict['username'],'pwd':specDict['password']}}}
    tokenResponse = requests.post(tokenURL, json=jsonPayload, verify=False)
    jsonData = tokenResponse.json()
    token = jsonData["imdata"][0]["aaaLogin"]["attributes"]["token"]
    cookie = {'APIC-cookie':token}
    controllerFwPol = baseURL + "/api/node/class/firmwareCtrlrFwP.json"
    uploadHeader = {"content-type": "application/json"}
    #uploadName = "apic-" + str(randint(0, 10))
    #uploadDn = "uni/fabric/fwrepop/osrc-" + uploadName
    for i in range(len(switchInventoryDict)):
        if("n9000" in switchInventoryDict[i]['aciSoftware']):
            switchUpgradeVersion = switchInventoryDict[i]['aciSoftware']
            print(switchUpgradeVersion)
    switchUpgradeURL = baseURL + "/api/node/mo/uni/fabric.json"
    print(switchUpgradeURL)
    #print(switchFWPolGrpPayload)

#    for i in range(len(switchInventoryDict)):
#       if(int(switchInventoryDict[i]['nodeID']) % 2 == 0):
#            nodeBlkName = "NODEBLK-" + switchInventoryDict[i]['nodeID']
#            switchFWPolGrpPayload = {"fabricInst":{"attributes":{"dn":"uni/fabric","status":"modified"},"children":[{"maintMaintP":{"attributes":{"dn":"uni/fabric/maintpol-evenNodes","version":switchUpgradeVersion,"ignoreCompat":"true","adminSt":"triggered","runMode":"pauseOnlyOnFailures"},"children":[]}},{"maintMaintGrp":{"attributes":{"name":"evenNodes"},"children":[{"fabricNodeBlk":{"attributes":{"name":nodeBlkName,"from_":switchInventoryDict[i]['nodeID'],"to_":switchInventoryDict[i]['nodeID']}}},{"maintRsMgrpp":{"attributes":{"tnMaintMaintPName":"evenNodes"}}}]}}]}}
#            switchFwPolGrp = requests.post(switchUpgradeURL, json=switchFWPolGrpPayload, cookies=cookie, verify=False)
#            print(switchFWPolGrpPayload)
#            print(switchFwPolGrp)
#            print("Break")

    for i in range(len(switchInventoryDict)):
        if(int(switchInventoryDict[i]['nodeID']) % 2 != 0):
            nodeBlkName = "NODEBLK-" + switchInventoryDict[i]['nodeID']
            switchFWPolGrpPayload = {"fabricInst":{"attributes":{"dn":"uni/fabric","status":"modified"},"children":[{"maintMaintP":{"attributes":{"dn":"uni/fabric/maintpol-oddNodes","version":switchUpgradeVersion,"ignoreCompat":"true","adminSt":"triggered","runMode":"pauseOnlyOnFailures"},"children":[]}},{"maintMaintGrp":{"attributes":{"name":"oddNodes"},"children":[{"fabricNodeBlk":{"attributes":{"name":nodeBlkName,"from_":switchInventoryDict[i]['nodeID'],"to_":switchInventoryDict[i]['nodeID']}}},{"maintRsMgrpp":{"attributes":{"tnMaintMaintPName":"oddNodes"}}}]}}]}}
            switchFwPolGrp = requests.post(switchUpgradeURL, json=switchFWPolGrpPayload, cookies=cookie, verify=False)
            print(switchFWPolGrpPayload)
            print(switchFwPolGrp)
            print("Break")

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
    apicUpgradeResult = apicUpgrade(cliArgs)