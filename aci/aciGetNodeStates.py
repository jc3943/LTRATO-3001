# Jeff Comer
# script to check apic and switch status

import urllib.request
import urllib3
import sys, time
import getopt
import requests
import csv, json, pprint
import random
from random import seed
from aciOps import bakeCookies
from aciOps import getApicStatus
from aciOps import getNodeStatus

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

    argDict = {"username":"","password":"","hostIp":"","infile":""}
    try:
      opts, args = getopt.getopt(argv,"hu:p:i:f:",["username","password","hostIp=","infile="])
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
      elif opt in ("-f", "--infile"):
         file = arg
         argDict["infile"] = file
    return argDict

if __name__ == '__main__':
    apicHealth = False
    cliArgs = main(sys.argv[1:])
    apicSnacks = bakeCookies(cliArgs)
    apicStatusResult = getApicStatus(cliArgs, apicSnacks)
    nodeStatusResult = getNodeStatus(cliArgs, apicSnacks)
    if(apicStatusResult == []):
        apicHealth == True
        print("APIC'S ARE FULLY FIT")
    else:
        apicHealth == False
        print("SOME OR APIC'S ARE NOT FULLY FIT\n", apicStatusResult)