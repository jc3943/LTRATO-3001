# Jeff Comer
# Collection of Intersight functions

import sys, getopt, csv
import requests, json
import urllib3
from intersight_auth import IntersightAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create an AUTH object
AUTH = IntersightAuth(
    secret_key_filename='creds/qa-isight-SecretKey.txt',
    api_key_id='6273ddc07564612d30091b97/6273e4cc7564612d300964b9/62f53d6e7564612d30253ff4'
    )

def getDevTargetStatus(specDict):
    i = 0
    targetURL = specDict['url'] + "/api/v1/asset/Targets"
    targetClaimStatus = requests.get(targetURL, verify=False, auth=AUTH)
    print(targetClaimStatus.text)
    targetClaimStatusJson = targetClaimStatus.json()
    print(len(targetClaimStatusJson["Results"]))
    for i in range(len(targetClaimStatusJson["Results"])):
        if (targetClaimStatusJson["Results"][i]["TargetType"] != "IntersightAppliance"):
            print(targetClaimStatusJson["Results"][i]["Status"])

def deployHXProfiles(specDict):
    profileURL = specDict['url'] + "/api/v1/hyperflex/ClusterProfiles"
    #print(profileURL)
    response = requests.get(profileURL, verify=False, auth=AUTH)
    hxProfileJson = response.json()
    profileMoid =  hxProfileJson["Results"][0]["Moid"]
    profileDeployURL = profileURL + "/" + profileMoid
    profileDeployPayload = {"Action":"Deploy"}
    profileDeployResponse = requests.post(profileDeployURL, json=profileDeployPayload, verify=False, auth=AUTH)
    print(profileDeployResponse.text)

