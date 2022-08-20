# Jeff Comer
# script to apply stigs to Hyperflex
# Example input file is vars/<branch>/hx-ctrlvm.csv

import sys, getopt, csv
import requests, json
import urllib3
from hxOps import  hxGetStigStat, hxGetToken, hxConfigStig, hxRemoveStig

def main(argv):
    """
    Main execution routine

    :return: None
    """

    username = ""
    password = ""
    userArg = ""
    pwArg = ""

    argDict = {"username":"","password":"","infile":""}
    try:
      opts, args = getopt.getopt(argv,"hu:p:i:",["username","password","infile="])
    except getopt.GetoptError:
      print('hx-stig.py -u <username> -p <password> -i <inputcsv>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('hx-stig.py -u <username> -p <password> -i <inputcsv>')
         sys.exit()
      elif opt in ("-u", "--username"):
         userArg = arg
         argDict["username"] = userArg
      elif opt in ("-p", "--password"):
         pwArg = arg
         argDict["password"] = pwArg
      elif opt in ("-i", "--infile"):
         infileArg = arg
         argDict["infile"] = infileArg
    return argDict

if __name__ == '__main__':
    hxData = main(sys.argv[1:])
    hxToken = hxGetToken(hxData)
    hxStigCheck = hxGetStigStat(hxData, hxToken)
    #hxStigApply = hxConfigStig(hxData, hxToken)
    hxStigRemove = hxRemoveStig(hxData, hxToken)