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
from aciOps import bakeCookies

def switchUpgrade(specDict):
    jsonPayload = ""
    payloadURL = ""
    evenNodesList = []
    oddNodesList = []

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
    #print(switchFWPolGrpPayload)

    if (specDict['nodeGrp'] == "evenNodes"):
        for i in range(len(switchInventoryDict)):
            if (int(switchInventoryDict[i]['nodeID']) != ''):
                if((int(switchInventoryDict[i]['nodeID'])) % 2 == 0):
                    evenNodesList.append(int(switchInventoryDict[i]['nodeID']))
                    nodeBlkName = "NODEBLK-" + switchInventoryDict[i]['nodeID']
                    switchFWPolGrpPayload = {"fabricInst":{"attributes":{"dn":"uni/fabric","status":"modified"},"children":[{"maintMaintP":{"attributes":{"dn":"uni/fabric/maintpol-evenNodes","version":switchUpgradeVersion,"ignoreCompat":"true","adminSt":"triggered","runMode":"pauseOnlyOnFailures"},"children":[]}},{"maintMaintGrp":{"attributes":{"name":"evenNodes"},"children":[{"fabricNodeBlk":{"attributes":{"name":nodeBlkName,"from_":switchInventoryDict[i]['nodeID'],"to_":switchInventoryDict[i]['nodeID']}}},{"maintRsMgrpp":{"attributes":{"tnMaintMaintPName":"evenNodes"}}}]}}]}}
                    switchFwPolGrp = requests.post(switchUpgradeURL, json=switchFWPolGrpPayload, cookies=cookie, verify=False)
        print("Upgrading Even Node Grp:\t", evenNodesList)
        return evenNodesList


    if (specDict['nodeGrp'] == "oddNodes"):
        for i in range(len(switchInventoryDict)):
            if (switchInventoryDict[i]['nodeID'] != ''):
                if(int(switchInventoryDict[i]['nodeID']) % 2 != 0):
                    print(int(switchInventoryDict[i]['nodeID']))
                    oddNodesList.append(switchInventoryDict[i]['nodeID'])
                    nodeBlkName = "NODEBLK-" + switchInventoryDict[i]['nodeID']
                    switchFWPolGrpPayload = {"fabricInst":{"attributes":{"dn":"uni/fabric","status":"modified"},"children":[{"maintMaintP":{"attributes":{"dn":"uni/fabric/maintpol-oddNodes","version":switchUpgradeVersion,"ignoreCompat":"true","adminSt":"triggered","runMode":"pauseOnlyOnFailures"},"children":[]}},{"maintMaintGrp":{"attributes":{"name":"oddNodes"},"children":[{"fabricNodeBlk":{"attributes":{"name":nodeBlkName,"from_":switchInventoryDict[i]['nodeID'],"to_":switchInventoryDict[i]['nodeID']}}},{"maintRsMgrpp":{"attributes":{"tnMaintMaintPName":"oddNodes"}}}]}}]}}
                    switchFwPolGrp = requests.post(switchUpgradeURL, json=switchFWPolGrpPayload, cookies=cookie, verify=False)
        print(switchFwPolGrp)
        print("Upgrading Odd Node Grp:\t", oddNodesList)
        return oddNodesList

def checkNodeUpgStatus(specDict, nodeList):
    with open(specDict['file'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        switchInventoryDict = list(csvread)

    completedNodeList = []
    upgradeComplete = False

    baseURL = "https://" + specDict['hostIp']
    nodeStatusURL = baseURL + "/api/node/class/maintUpgJob.json"
    maintGrp = specDict['nodeGrp']

    for upgradeCheck in range(0, 90):
        try:
            cookie = bakeCookies(specDict)
            try:
                upgradeStatus = requests.get(nodeStatusURL, cookies=cookie, verify=False)
                upgradeStatusJson = upgradeStatus.json()
                for i in range(len(upgradeStatusJson['imdata'])):
                    if (upgradeStatusJson['imdata'][i]['maintUpgJob']['attributes']['maintGrp'] == maintGrp):
                        if (int(upgradeStatusJson['imdata'][i]['maintUpgJob']['attributes']['maintGrp'] == maintGrp) == 100):
                            print("Upgrade Complete for:\t", upgradeStatusJson['imdata'][i]['maintUpgJob']['attributes']['maintGrp'])
                            upgradeComplete = True
                            break
                        else:
                            print("Upgrade Progress: ", upgradeStatusJson['imdata'][i]['maintUpgJob']['attributes']['maintGrp'], upgradeStatusJson['imdata'][i]['maintUpgJob']['attributes']['instlProgPct'])
                            upgradeCheck += 1
                            time.sleep(60)
            except:
                print("Failed to acquire upgrade status")
                upgradeCheck += 1
                time.sleep(60)


        except:
            print("Unable to acquire API token")
            upgradeCheck += 1
            time.sleep(60)
        time.sleep(60)
    return upgradeComplete


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

    argDict = {"username":"","password":"","hostIp":"","file":"","nodeGrp":""}
    try:
      opts, args = getopt.getopt(argv,"hu:p:i:f:n:",["username","password","hostIp=","file=","nodeGrp="])
    except getopt.GetoptError:
      print('apicUpgrade.py -u <username> -p <password> -i <host_ip> -f <inputfile>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('apicUpgrade.py -u <username> -p <password> -i <host_ip> -f <inputfile> -n <evenNodes or oddNodes')
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
      elif opt in ("-n", "--nodeGrp"):
         nodeGrp = arg
         argDict["nodeGrp"] = nodeGrp
    return argDict

if __name__ == '__main__':
    cliArgs = main(sys.argv[1:])
    switchUpgradeResult = switchUpgrade(cliArgs)
    upgradeStatus = checkNodeUpgStatus(cliArgs, switchUpgradeResult)