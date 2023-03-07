# Jeff Comer
# script to get Insight Server Profiles

import sys, getopt, csv
import requests, json
import urllib3
from intersight_auth import IntersightAuth
from intersightOps import deployHXProfiles, statusHXDeploy


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
         print('intersightProfiles.py -u <intersightURL>')
         sys.exit()
      elif opt in ("-u", "--url"):
         userArg = arg
         argDict["url"] = userArg
    return argDict

if __name__ == '__main__':
    hxData = main(sys.argv[1:])
    hxProfiles = deployHXProfiles(hxData)
    hxDeployState = statusHXDeploy(hxData)
