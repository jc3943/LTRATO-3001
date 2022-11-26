#Jeff Comer
#Script to shut/noshut ports in ACI fabric - example seed file in vars/<branch>/portOps.csv

import urllib.request
import urllib3
import sys
import getopt
import requests
import csv, json
from aciOps import hxPortActions, bakeCookies

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
    actionResult = hxPortActions(cliArgs)
    

    