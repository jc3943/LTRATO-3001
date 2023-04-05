#!/usr/bin/python3
#written by Jeff Comer - script to test check http status from a csv file of hosts
# example input file vars/<branch>/ipAddresses.csv

import time
import urllib.request
import psycopg2
import ssl
import sys
"""
"""
import csv, sys, getopt

def get_responses(argList):
    cimcList = []
    esxiList = []
    allList = []
    errorList = []
    httpResult = ""
    with open(argList[0], 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        addrListDict = list(csvread)
        #print(addrListDict)
    for cimc in addrListDict:
        if (cimc['CIMC'] != ""):
            cimcList.append(cimc['CIMC'])
    for esxi in addrListDict:
        if (esxi['ESXI'] != ""):
            esxiList.append(esxi['ESXI'])
    allList = cimcList + esxiList
    #print(cimcList)
    #print(esxiList)
    #print(allList)
    if (argList[1] == 'cimc'):
        for i in range(len(addrListDict)):
            urls = "https://" + addrListDict[i]['cimc']
            #print("Testing http connection to: " + urls)
            context = ssl._create_unverified_context()
            try:
                resp = urllib.request.urlopen(urls, context=context, timeout = 4)
                code = resp.getcode()
                httpResult = urls + ":  " + str(code)
                if code == 200:
                    print(httpResult)
                    #return True
                elif code != 200:
                    errorList.append(urls + ": Failed")
                    errorLog = open("./errors.log", "a")
                    errorLog.write(httpResult)
                    errorLog.close()
                    #return False
            except:
                #print("Connection Failed\n")
                errorList.append(urls + ": Failed")
                errorLog = open("./errors.log", "a")
                errorLog.write(urls + ": Failed\n")
                errorLog.close()
    if (argList[1] == 'esxi'):
        for i in range(len(addrListDict)):
            urls = "https://" + addrListDict[i]['esxi']
            #print("Testing http connection to: " + urls)
            context = ssl._create_unverified_context()
            try:
                resp = urllib.request.urlopen(urls, context=context, timeout = 4)
                code = resp.getcode()
                httpResult = urls + ":  " + str(code)
                if code == 200:
                    print(httpResult)
                    #return True
                elif code != 200:
                    errorList.append(urls + ": Failed")
                    errorLog = open("./errors.log", "a")
                    errorLog.write(httpResult)
                    errorLog.close()
                    #return False
            except:
                #print("Connection Failed\n")
                errorList.append(urls + ": Failed")
                errorLog = open("./errors.log", "a")
                errorLog.write(urls + ": Failed\n")
                errorLog.close()
    if (argList[1] == 'all'):
        for i in range(len(allList)):
            urls = "https://" + allList[i]
            #print("Testing http connection to: " + urls)
            context = ssl._create_unverified_context()
            try:
                resp = urllib.request.urlopen(urls, context=context, timeout = 4)
                code = resp.getcode()
                httpResult = urls + ":  " + str(code)
                if code == 200:
                    print(httpResult)
                    #return True
                elif code != 200:
                    errorList.append(urls + ": Failed")
                    errorLog = open("./errors.log", "a")
                    errorLog.write(httpResult)
                    errorLog.close()
                    #return False
            except:
                errorList.append(urls + ": Failed")
                errorLog = open("./errors.log", "a")
                errorLog.write(urls + ": Failed\n")
                errorLog.close()
    if (len(errorList) == 0):
        return True
    elif (len(errorList) != 0):
        return False
    

def main(argv):
    """
    Main execution routine

    :return: None
    """

    inputfile = ""
    outputfile = ""
    opAction = ""
    opList = []
    try:
      opts, args = getopt.getopt(argv,"hi:a:",["ifile=","action="])
    except getopt.GetoptError:
      #print('oob-preOp-http.py -i <inputfile> -a <cimc, esxi, or all>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('oob-preOp-http.py -i <inputfile> -a <cimc, esxi, or all>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
         opList.append(inputfile)
      elif opt in ("-a", "--action"):
         opAction = arg
         opList.append(opAction)
    return opList

if __name__ == '__main__':
    fileActionData = main(sys.argv[1:])
    http_test = get_responses(fileActionData)
    #print(http_test)
    if http_test == True:
        print("Success")
        sys.exit(0)
    else:
        print("Failed - Check errors.log for details")
        sys.exit(-1)


