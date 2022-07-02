from k8sOps import getNodes
import json

if __name__ == '__main__':
    nodeList = getNodes()
    print(json.dumps(nodeList))
