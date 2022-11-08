# Jeff Comer
# script to set admin password IMC
# Example input file is vars/<branch>/imc/hostIpAddrs.csv

import sys, getopt, csv
import requests, json
import urllib3
from imcOps import imcAdminPw


def main(argv):
    """
    Main execution routine

    :return: None
    """

    username = ""
    password = ""
    userArg = ""
    pwArg = ""

    argDict = {"username":"","password":"","infile":"","newPw":""}
    try:
      opts, args = getopt.getopt(argv,"hu:p:i:n:",["username","password","infile=","newPw"])
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
      elif opt in ("-n", "--newPw"):
         infileArg = arg
         argDict["newPw"] = infileArg
    return argDict

if __name__ == '__main__':
    cimcData = main(sys.argv[1:])
    imcAdminPw = imcAdminPw(cimcData)