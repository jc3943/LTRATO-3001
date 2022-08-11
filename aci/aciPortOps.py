#Jeff Comer
#Script to shut/noshut ports in ACI fabric - example seed file in vars/<branch>/portOps.csv

import urllib.request
import urllib3
import sys
import getopt
import requests
import csv, json

def portActions(specDict):
    jsonPayload = ""

    with open(specDict['file'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        portNodeDict = list(csvread)
    print(portNodeDict)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    tokenURL = "https://" + specDict['hostIp'] + "/api/aaaLogin.json"
    portURL = "https://" + specDict['hostIp'] + "/api/node/mo/uni/fabric/outofsvc.json"
    tokenHeader = {"content-type": "application/json"}
    jsonPayload = {'aaaUser':{"attributes":{'name':specDict['username'],'pwd':specDict['password']}}}
    tokenResponse = requests.post(tokenURL, json=jsonPayload, verify=False)
    jsonData = tokenResponse.json()
    token = jsonData["imdata"][0]["aaaLogin"]["attributes"]["token"]
    cookie = {'APIC-cookie':token}
    if(specDict['action'] == "shut"):
       for i in range(len(portNodeDict)):
          portJson = "{\"fabricRsOosPath\":{\"attributes\":{\"tDn\":\"topology/pod-1/paths-" + portNodeDict[i]['node'] + "/pathep-[eth1/" + portNodeDict[i]['port'] + "]\",\"lc\":\"blacklist\"},\"children\":[]}}"
          portShut = requests.post(portURL, json=json.loads(portJson), cookies=cookie, verify=False)
          #portShut = requests.post(portURL, json={"fabricRsOosPath":{"attributes":{"tDn":"topology/pod-1/paths-201/pathep-[eth1/15]","lc":"blacklist"},"children":[]}}, cookies=cookie, verify=False)
                                                 #{"fabricRsOosPath":{"attributes":{"tDn":"topology/pod-1/paths-201/pathep-[eth1/15]","lc":"blacklist"},"children":[]}}
    #port shutdown url and payload
    #url: https://172.16.20.7/api/node/mo/uni/fabric/outofsvc.json
    #payload{"fabricRsOosPath":{"attributes":{"tDn":"topology/pod-1/paths-201/pathep-[eth1/15]","lc":"blacklist"},"children":[]}}
    if(specDict['action'] == "noshut"):
       for i in range(len(portNodeDict)):
          portJson = "{\"fabricRsOosPath\":{\"attributes\":{\"dn\":\"uni/fabric/outofsvc/rsoosPath-[topology/pod-1/paths-" + portNodeDict[i]['node'] + "/pathep-[eth1/" + portNodeDict[i]['port'] + "]]\",\"status\":\"deleted\"},\"children\":[]}}"
          print(portJson)
          portNoShut = requests.post(portURL, json=json.loads(portJson), cookies=cookie, verify=False)
          #portNoShut = requests.post(portURL, json={"fabricRsOosPath":{"attributes":{"dn":"uni/fabric/outofsvc/rsoosPath-[topology/pod-1/paths-201/pathep-[eth1/15]]","status":"deleted"},"children":[]}}, cookies=cookie, verify=False)
                                                   #{"fabricRsOosPath":{"attributes":{"dn":"uni/fabric/outofsvc/rsoosPath-[topology/pod-1/paths-206/pathep-[eth1/24]","status":"deleted"},"children":[]}}
    #port no shut url and payload
    #url: https://172.16.20.7/api/node/mo/uni/fabric/outofsvc.json
    #payload{"fabricRsOosPath":{"attributes":{"dn":"uni/fabric/outofsvc/rsoosPath-[topology/pod-1/paths-201/pathep-[eth1/15]]","status":"deleted"},"children":[]}}
    

def main(argv):
    """
    Main execution routine

    :return: None
    """

    file = ""
    username = ""
    password = ""
    hostIp = ""
    action = ""
    opAction = ""
    argDict = {"username":"","password":"","hostIp":"","file":"","action":""}
    try:
      opts, args = getopt.getopt(argv,"hu:p:i:f:a:",["user=","password=","hostIp=","file=","action="])
    except getopt.GetoptError:
      print('aciPortOps.py -u <username> -p <password> -i <host_ip> -f <inputfile> -a <action (shut or noshut)>)')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('aciPortOps.py -u <username> -p <password> -i <host_ip> -f <inputfile> -a <action (shut or noshut)>)')
         sys.exit()
      elif opt in ("-u", "--user"):
         username = arg
         argDict["username"] = username
      elif opt in ("-p", "--password"):
         password = arg
         argDict["password"] = password
      elif opt in ("-i", "--hostIp"):
         hostIp = arg
         argDict["hostIp"] = hostIp
      elif opt in ("-f", "--file"):
         file = arg
         argDict["file"] = file
      elif opt in ("-a", "--action"):
         action = arg
         argDict["action"] = action
    return argDict

if __name__ == '__main__':
    cliArgs = main(sys.argv[1:])
    actionResult = portActions(cliArgs)
    

    