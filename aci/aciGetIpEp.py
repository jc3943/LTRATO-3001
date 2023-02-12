# Jeff Comer
# script to collect fabric endpoint data

import urllib.request
import urllib3
import sys, time
import getopt
import requests
import csv, json, pprint
import random
from aciOps import bakeCookies
from aciOps import getAciIpEp


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

    argDict = {"username":"","password":"","hostIp":""}
    try:
      opts, args = getopt.getopt(argv,"hu:p:i:",["username","password","hostIp="])
    except getopt.GetoptError:
      print('aciGetIpEp.py -u <username> -p <password> -i <host_ip>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('aciGetIpEp.py -u <username> -p <password> -i <host_ip>')
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
    return argDict

if __name__ == '__main__':
    apicHealth = False
    nodeHealth = False
    cliArgs = main(sys.argv[1:])
    apicSnacks = bakeCookies(cliArgs)
    apicIpepResult = getAciIpEp(cliArgs, apicSnacks)


    