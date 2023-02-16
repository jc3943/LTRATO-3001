import urllib.request
import urllib3
import sys, time, os
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
            print("Disabling ports on: " + portNodeDict[i]['name'] + "\t" + portNodeDict[i]['toPort'])
            for j in range(len(nodeList)):
                portJson = {"fabricRsOosPath":{"attributes":{"tDn":"topology/pod-1/paths-" + nodeList[j] + "/pathep-[eth1/" + portNodeDict[i]['toPort'] + "]","lc":"blacklist"},"children":[]}}
                print(portJson)
                portShut = requests.post(portURL, json=portJson, cookies=cookie, verify=False)
                print(portShut)

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

def getApicStatus(specDict, apicSnacks):
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    i = 0
    j = 0
    apicFitList = []
    apicFitDict = {}
    apicUnFitList = []
    apicUnFitDict = {}

    baseURL = "https://" + specDict['hostIp']
    for i in range(len(csvDict)):
        if (csvDict[i]['apicNodeId'] != ''):
            apicStatusURL = baseURL + "/api/node/mo/topology/pod-1/node-" + str(csvDict[i]['apicNodeId']) + ".json?query-target=subtree&target-subtree-class=infraWiNode"
            cookie = apicSnacks
            apicStatusResponse = requests.get(apicStatusURL, cookies=cookie, verify=False)
            apicStatusJson = apicStatusResponse.json()
            for j in range(len(apicStatusJson['imdata'])):
                if (apicStatusJson['imdata'][j]['infraWiNode']['attributes']['health'] == "fully-fit"):
                    apicFitDict = {'nodeName':apicStatusJson['imdata'][j]['infraWiNode']['attributes']['nodeName'], 'nodeState':apicStatusJson['imdata'][j]['infraWiNode']['attributes']['health']}
                    apicFitList.append(apicFitDict)
                else:
                    apicUnFitDict = {'nodeName':apicStatusJson['imdata'][j]['infraWiNode']['attributes']['nodeName'], 'nodeState':apicStatusJson['imdata'][j]['infraWiNode']['attributes']['health']}
                    apicUnFitList.append(apicFitDict)

    print(apicFitList)
    print(apicUnFitList)
    return apicUnFitList

def getNodeStatus(specDict, apicSnacks):
    i = 0
    nodeFitList = []
    nodeFitDict = {}
    nodeUnFitList = []
    nodeUnFitDict = {}

    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    baseURL = "https://" + specDict['hostIp']
    nodeStatusURL = baseURL + "/api/node/mo/topology/pod-1.json?query-target=children&target-subtree-class=fabricNode"
    cookie = apicSnacks
    nodeStatusResponse = requests.get(nodeStatusURL, cookies=cookie, verify=False)
    nodeStatusJson = nodeStatusResponse.json()
    for i in range(len(nodeStatusJson['imdata'])):
        if (nodeStatusJson['imdata'][i]['fabricNode']['attributes']['role'] == "leaf" or nodeStatusJson['imdata'][i]['fabricNode']['attributes']['role'] == "spine"):
            if (nodeStatusJson['imdata'][i]['fabricNode']['attributes']['fabricSt'] ==  "active"):
                nodeFitDict = {'nodeName':nodeStatusJson['imdata'][i]['fabricNode']['attributes']['name'], 'state':nodeStatusJson['imdata'][i]['fabricNode']['attributes']['fabricSt']}
                nodeFitList.append(nodeFitDict)
            else:
                nodeUnFitDict = {'nodeName':nodeStatusJson['imdata'][i]['fabricNode']['attributes']['name'], 'state':nodeStatusJson['imdata'][i]['fabricNode']['attributes']['fabricSt']}
                nodeUnFitList.append(nodeUnFitDict)
    print(nodeFitList)
    print(nodeUnFitList)
    return nodeUnFitList

def getAciIpEp(specDict, apicSnacks):

    fvIpEpListoDicts = []
    fvIpEpDict = {'ipAddress':'', 'macAddress':'', 'tenant':'', 'BD':'', 'EPG':''}
    outfilepath = os.environ['varPath']
    outfile = outfilepath + "/aci/aciEpData.csv"

    baseURL = "https://" + specDict['hostIp']
    fvCEpURL = baseURL + "/api/node/class/fvCEp.json?query-target=children&target-subtree-class=fvIp"
    cookie = apicSnacks
    aciIpEpResponse = requests.get(fvCEpURL, cookies=cookie, verify=False)
    aciIpEpJson = aciIpEpResponse.json()
    for i in range(len(aciIpEpJson['imdata'])):
        if (aciIpEpJson['imdata'][i]['fvIp']['attributes']['bdDn'] != ""):
            epIp = aciIpEpJson['imdata'][i]['fvIp']['attributes']['addr']
            bdDn = aciIpEpJson['imdata'][i]['fvIp']['attributes']['bdDn']
            firstSplit = bdDn.split("/")
            tenantSplit = firstSplit[1].split("-")
            tenant = tenantSplit[1]
            bdSplit = firstSplit[2].split("-") 
            bridgeDomain = bdSplit[1]
            dn = bdDn = aciIpEpJson['imdata'][i]['fvIp']['attributes']['dn']
            dnSplit = dn.split("/")
            epgSplit = dnSplit[3].split("-")
            egp = epgSplit[1]
            macSplit = dnSplit[4].split("-")
            mac = macSplit[1]
            fvIpEpDict = {'ipAddress':epIp, 'macAddress':mac, 'tenant':tenant, 'BD':bridgeDomain, 'EPG':egp}
            fvIpEpListoDicts.append(fvIpEpDict)
            print(fvIpEpDict)

    keys = fvIpEpListoDicts[0].keys()
    with open(outfile, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(fvIpEpListoDicts)
    return fvIpEpListoDicts

def getTenants(specDict, apicSnacks):
    tenantList = []
    baseURL = "https://" + specDict['hostIp']
    tenantURL = baseURL + "/api/node/class/fvTenant.json"
    cookie = apicSnacks
    tenantResponse = requests.get(tenantURL, cookies=cookie, verify=False)
    tenantJson = tenantResponse.json()
    for i in range(len(tenantJson['imdata'])):
        if (tenantJson['imdata'][i]['fvTenant']['attributes']['name'] == "infra" or tenantJson['imdata'][i]['fvTenant']['attributes']['name'] == "common" or tenantJson['imdata'][i]['fvTenant']['attributes']['name'] == "mgmt"):
            print("Ignoring default tenants", tenantJson['imdata'][i]['fvTenant']['attributes']['name'])
        else:
            tenantList.append(tenantJson['imdata'][i]['fvTenant']['attributes']['name'])

    return tenantList

def getTenantBDs(specDict, apicSnacks, tenants):
    bdDict = {'bridgeDomain':'', 'gateway':'', 'prefixLength':'', 'tenant':''}
    bdDictList = []
    baseURL = "https://" + specDict['hostIp']
    cookie = apicSnacks
    for i in range(len(tenants)):
        tenantBDURL = baseURL + "/api/node/mo/uni/tn-" + tenants[i] + ".json?query-target=children&target-subtree-class=fvBD"
        tenantBDResponse = requests.get(tenantBDURL, cookies=cookie, verify=False)
        tenantBDJson = tenantBDResponse.json()
        #print(tenantBDJson)
        for k in range(len(tenantBDJson['imdata'])):
            bdDataURL = baseURL + "/api/node/mo/uni/tn-" + tenants[i] + "/BD-" + tenantBDJson['imdata'][k]['fvBD']['attributes']['name'] + ".json?query-target=children&target-subtree-class=fvSubnet"
            print(bdDataURL)
            bdDataResponse = requests.get(bdDataURL, cookies=cookie, verify=False)
            bdDataJson = bdDataResponse.json()
            ipSpecs = bdDataJson['imdata'][0]['fvSubnet']['attributes']['ip']
            ipSpecSplit = ipSpecs.split("/")
            gwAddr = ipSpecSplit[0]
            prefixLength = ipSpecSplit[1]
            bdDict = {'bridgeDomain':tenantBDJson['imdata'][k]['fvBD']['attributes']['name'], 'gateway':gwAddr, 'prefixLength':prefixLength, 'tenant':tenants[i]}
            bdDictList.append(bdDict)
    print(bdDictList)
