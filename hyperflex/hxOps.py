# Jeff Comer
# script collection for Hyperflex
# Example input file is vars/<branch>/hx-ctrlvm.csv

import sys, getopt, csv
import requests, json, jsonschema
from jsonschema import validate
import urllib3, pprint

def validataJson(jsonData, schemaData):
    try:
        validate(instance=jsonData, schema=schemaData)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

def hxGetToken(specDict):
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        tokenURL = "https://" + csvDict[i]['host'] + "/aaa/v1/auth?grant_type=password"
        authPayload = {"username":specDict['username'],"password":specDict['password']}
        tokenResponse = requests.post(tokenURL, json=authPayload, verify=False)
        tokenJson = tokenResponse.json()
        print("Token Acquired", tokenResponse, sep=":")
        token = tokenJson["access_token"]
    return token

def hxGetCuuid(specDict, token):
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        clusterInfoURL = "https://" + csvDict[i]['host'] + "/coreapi/v1/clusters"
        bearerStr = "Bearer " + token
        clusterInfoHeader = {"Authorization":bearerStr}
        clusterInfoResponse = requests.get(clusterInfoURL, headers=clusterInfoHeader, verify=False)
        clusterInfoJson = clusterInfoResponse.json()
        cuuid = clusterInfoJson[0]["uuid"]
        print("CUUID Acquired", clusterInfoResponse, sep=":")
        return cuuid

def hxGetClusterState(specDict, token, cuuid):
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        clusterStatURL = "https://" + csvDict[i]['host'] + "/coreapi/v1/clusters/" + cuuid + "/health"
        bearerStr = "Bearer " + token
        clusterInfoHeader = {"Authorization":bearerStr}
        clusterStatResponse = requests.get(clusterStatURL, headers=clusterInfoHeader, verify=False)
        clusterStatJson = clusterStatResponse.json()
        pprint.pprint(clusterStatJson)

def hxGetHostInfo(specDict, token):
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        hostInfoURL = "https://" + csvDict[i]['host'] + "/coreapi/v1/hypervisor/hosts"
        bearerStr = "Bearer " + token
        hostInfoHeader = {"Authorization":bearerStr}
        hostInfoResponse = requests.get(hostInfoURL, headers=hostInfoHeader, verify=False)
        hostInfoJson = hostInfoResponse.json()
        #print(json.dumps(hostInfoJson))
        hostInfoFile = "../data/" + csvDict[i]['host'] + "-hosts.json"
        with open(hostInfoFile, 'w') as f:
            json.dump(hostInfoJson, f)

def hxGetDiskInfo(specDict, token):
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        hostDiskURL = "https://" + csvDict[i]['host'] + "/coreapi/v1/hypervisor/disks"
        bearerStr = "Bearer " + token
        hostDiskHeader = {"Authorization":bearerStr}
        hostDiskResponse = requests.get(hostDiskURL, headers=hostDiskHeader, verify=False)
        hostDiskJson = hostDiskResponse.json()
        #print(json.dumps(hostDiskJson))
        diskInfoFile = "../data/" + clusterVip + "-disks.json"
        with open(diskInfoFile, 'w') as f:
            json.dump(hostDiskJson, f)

def hxGetStigStat(specDict, token):
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        stigStatURL = "https://" + csvDict[i]['host'] + "/supportservice/v1/stig/check"
        bearerStr = "Bearer " + token
        stigStatHeader = {"Authorization":bearerStr}
        stigStatResponse = requests.put(stigStatURL, headers=stigStatHeader, verify=False)
        stigStatJson = stigStatResponse.json()
        print(stigStatJson)

def hxConfigStig(specDict, token):
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        configStigURL = "https://" + csvDict[i]['host'] + "/supportservice/v1/stig/apply"
        bearerStr = "Bearer " + token
        configStigHeader = {"Authorization":bearerStr}
        configStigResponse = requests.put(configStigURL, headers=configStigHeader, verify=False)
        configStigJson = configStigResponse.json()
        print(configStigJson)

def hxRemoveStig(specDict, token):
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        removeStigURL = "https://" + csvDict[i]['host'] + "/supportservice/v1/stig/remove"
        bearerStr = "Bearer " + token
        removeStigHeader = {"Authorization":bearerStr}
        removeStigResponse = requests.put(removeStigURL, headers=removeStigHeader, verify=False)
        removeStigJson = removeStigResponse.json()
        print(removeStigJson)

def hxCreateDatastore(specDict, token, cuuid):
    with open(specDict['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(len(csvDict)):
        hostDatastoreURL = "https://" + csvDict[i]['host'] + "/coreapi/v1/clusters/" + cuuid + "/datastores"
        print(hostDatastoreURL)
        bearerStr = "Bearer " + token
        hostDatastoreHeader = {"Authorization":bearerStr,"Content-type":"application/json","Accept":"application/json"}
        templateFile = open('./hyperflex/templates/datastore.json', 'rb')
        schemaFile = open('./hyperflex/schemas/datastore.schema')
        templateJson = json.load(templateFile)
        schemaJson = json.load(schemaFile)
        jsonTest = validataJson(templateJson, schemaJson)
        if jsonTest:
            hostDatastoreResponse = requests.post(hostDatastoreURL, headers=hostDatastoreHeader, json=templateJson, verify=False)
        else:
            print("Schema Validation Failure")
            exit(-1)
        print(hostDatastoreResponse)
