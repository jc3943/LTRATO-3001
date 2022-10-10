import urllib.request
import urllib3
import sys, time
import getopt
import requests
import csv, json, pprint
import random
from random import seed

def bakeCookies(specDict2):
    baseURL = "https://" + specDict2['hostIp']
    tokenURL = baseURL + "/api/aaaLogin.json"

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    tokenHeader = {"content-type": "application/json"}
    jsonPayload = {'aaaUser':{"attributes":{'name':specDict2['username'],'pwd':specDict2['password']}}}
    tokenResponse = requests.post(tokenURL, json=jsonPayload, verify=False)
    jsonData = tokenResponse.json()
    token = jsonData["imdata"][0]["aaaLogin"]["attributes"]["token"]
    newCookie = {'APIC-cookie':token}
    return newCookie

def hxPortActions(specDict):
    jsonPayload = ""

    with open(specDict['file'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        portNodeDict = list(csvread)
    #print(portNodeDict)

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
          #portJson = "{\"fabricRsOosPath\":{\"attributes\":{\"tDn\":\"topology/pod-1/paths-" + portNodeDict[i]['node'] + "/pathep-[eth1/" + portNodeDict[i]['port'] + "]\",\"lc\":\"blacklist\"},\"children\":[]}}"
          if(portNodeDict[i]['intfType'] == "vpc"):
            nodeList = portNodeDict[i]['node'].split("-")
            print("Disabling ports on: " + portNodeDict[i]['name'])
            for j in range(len(nodeList)):
                portJson = {"fabricRsOosPath":{"attributes":{"tDn":"topology/pod-1/paths-" + nodeList[j] + "/pathep-[eth1/" + portNodeDict[i]['toPort'] + "]","lc":"blacklist"},"children":[]}}
                portShut = requests.post(portURL, json=portJson, cookies=cookie, verify=False)

    if(specDict['action'] == "noshut"):
       for i in range(len(portNodeDict)):
          #portJson = "{\"fabricRsOosPath\":{\"attributes\":{\"dn\":\"uni/fabric/outofsvc/rsoosPath-[topology/pod-1/paths-" + portNodeDict[i]['node'] + "/pathep-[eth1/" + portNodeDict[i]['port'] + "]]\",\"status\":\"deleted\"},\"children\":[]}}"
          if(portNodeDict[i]['intfType'] == "vpc"):
            nodeList = portNodeDict[i]['node'].split("-")
            print("Enabling ports on: " + portNodeDict[i]['name'])
            for j in range(len(nodeList)):
                portJson = {"fabricRsOosPath":{"attributes":{"dn":"uni/fabric/outofsvc/rsoosPath-[topology/pod-1/paths-" + nodeList[j] + "/pathep-[eth1/" + portNodeDict[i]['toPort'] + "]]","status":"deleted"},"children":[]}}
                portNoShut = requests.post(portURL, json=portJson, cookies=cookie, verify=False)

def createTacacs(specDict, apicSnacks):
    baseURL = "https://" + specDict['hostIp']
    cookie = apicSnacks
    providerURL = baseURL + "/api/node/mo/uni/userext/tacacsext/tacacsplusprovider-172.16.5.1.json"
    loginDomainURL = baseURL + "/api/node/mo/uni/userext.json"
    providerPayload = {"aaaTacacsPlusProvider":{"attributes":{"dn":"uni/userext/tacacsext/tacacsplusprovider-172.16.5.1","name":"172.16.5.1","key":"THORP@ssw0rd!","rn":"tacacsplusprovider-172.16.5.1","status":"created"},"children":[{"aaaRsSecProvToEpg":{"attributes":{"tDn":"uni/tn-mgmt/mgmtp-default/oob-default","status":"created"},"children":[]}}]}}
    loginDomainPayload = {"aaaUserEp":{"attributes":{"dn":"uni/userext","status":"modified"},"children":[{"aaaLoginDomain":{"attributes":{"dn":"uni/userext/logindomain-tacacsLoginDomain","name":"tacacsLoginDomain","rn":"logindomain-tacacsLoginDomain","status":"created"},"children":[{"aaaDomainAuth":{"attributes":{"dn":"uni/userext/logindomain-tacacsLoginDomain/domainauth","realm":"tacacs","providerGroup":"tacacsLoginDomain","rn":"domainauth","status":"created"},"children":[]}}]}},{"aaaTacacsPlusEp":{"attributes":{"dn":"uni/userext/tacacsext","status":"modified"},"children":[{"aaaTacacsPlusProviderGroup":{"attributes":{"dn":"uni/userext/tacacsext/tacacsplusprovidergroup-tacacsLoginDomain","status":"created"},"children":[{"aaaProviderRef":{"attributes":{"dn":"uni/userext/tacacsext/tacacsplusprovidergroup-tacacsLoginDomain/providerref-172.16.5.1","order":"1","name":"172.16.5.1","status":"created"},"children":[]}}]}}]}}]}}
    providerResponse = requests.post(providerURL, json=providerPayload, cookies=cookie, verify=False)
    loginDomainResponse = requests.post(loginDomainURL, json=loginDomainPayload, cookies=cookie, verify=False)
    print(providerURL, providerResponse, sep=": ")
    print(loginDomainURL, loginDomainResponse, sep=": ")