# Jeff Comer
# script to get Insight Device Claim Status

import sys, getopt, csv
import requests, json
import urllib3
from intersight_auth import IntersightAuth
from intersightOps import getDevTargetStatus


def main(argv):
    """
    Main execution routine
    """

    argDict = {"url":""}
    try:
      opts, args = getopt.getopt(argv,"hu:",["url"])
    except getopt.GetoptError:
      print('intersightProfiles.py -u <intersightURL>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('imcVnicCreate.py -u <username> -p <password> -i <inputcsv>')
         sys.exit()
      elif opt in ("-u", "--url"):
         userArg = arg
         argDict["url"] = userArg
    return argDict

if __name__ == '__main__':
    hxData = main(sys.argv[1:])
    hxProfiles = getDevTargetStatus(hxData)