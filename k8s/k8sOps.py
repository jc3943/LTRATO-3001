from kubernetes import client, config
import json

def getNodes():
    nodeStatList = []
    nodeStatDict = {}
    nodeErrorDict = {}
    nodeErrorList = []
    config.load_kube_config()
    k8s_api = client.CoreV1Api()
    response = k8s_api.list_node()
    for i in range(len(response.items)):
        #print(response.items[i].metadata.name)
        numConditions = len(response.items[i].status.conditions)
        nodeStatDict = {"node":response.items[i].metadata.name, response.items[i].status.conditions[0].type:response.items[i].status.conditions[0].status}
        nodeStatDict.update({response.items[i].status.conditions[1].type:response.items[i].status.conditions[1].status})
        nodeStatDict.update({response.items[i].status.conditions[2].type:response.items[i].status.conditions[2].status})
        nodeStatDict.update({response.items[i].status.conditions[3].type:response.items[i].status.conditions[3].status})
        nodeStatList.append(nodeStatDict)
    return nodeStatList
 