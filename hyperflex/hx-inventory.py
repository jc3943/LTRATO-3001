# Jeff Comer
# script to gather HX Inventory Data
# Example input file is vars/<branch>/hx-ctrlvm.csv

import sys, getopt, csv
import requests, json
import urllib3
from hxOps import  hxGetToken, hxGetHostInfo, hxGetDiskInfo, hxGetCuuid

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
      print('cimcServerShutDown.py -u <username> -p <password> -i <inputcsv>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('cimcServerShutDown.py -u <username> -p <password> -i <inputcsv>')
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
    with open(hxData['infile'], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        csvDict = list(csvread)

    for i in range(len(csvDict)):
      hxToken = hxGetToken(hxData, csvDict[i]['host'])
      hxCuuid = hxGetCuuid(hxData, csvDict[i]['host'], hxToken)
      hxHostData = hxGetHostInfo(hxData, csvDict[i]['host'], hxToken)
      hxDiskData = hxGetDiskInfo(hxData, csvDict[i]['host'], hxToken)