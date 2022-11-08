# Jeff Comer
# script to set DNS form IMC
# Example input file is vars/<branch>/imc/hostIpAddrs.csv

import sys, getopt, csv
import requests, json
import urllib3
from imcOps import imcNetSet, imcNetProtSet


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
      opts, args = getopt.getopt(argv,"hu:p:i:n:",["username","password","infile="])
    except getopt.GetoptError:
      print('imcDns.py -u <username> -p <password> -i <inputcsv>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('imcDns.py -u <username> -p <password> -i <inputcsv>')
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
    cimcData = main(sys.argv[1:])
    imcDns = imcNetSet(cimcData)
    imcNetProt = imcNetProtSet(cimcData)