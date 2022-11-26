# Jeff Comer
# script to build vars/<branch>/switch-inventory.yaml using vars/<branch>/switch-inventory.csv

import yaml
from yaml import *
import os

import csv
from csv import *

import xlrd
from xlrd import *

from str2bool import str2bool

def main():
    # initialize all empty needed variables
    count = 0
    iter = 0
    setList = []
    longlist1 = []
    longlist2 = []
    longlist3 = []
    longlist4 = []
    longlist5 = []
    longlist6 = []
    overlist = []
    dicttwo = {}
    dict3 = {}

    infilepath = os.environ['varPath']
    outfilepath = os.environ['varPath']
    infile = infilepath + "/aci/switch-inventory.csv"
    outfile = outfilepath + "/aci/switch-inventory.yaml"

    # open the CSV file and read it's contents to a list of dictionaries
    with open(infile, 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        for column in csvread:
            # append each dict to the list
            setList.append(column)
            # make a list of keys (in this case it is all the columns)
            if count == 0:
                keyList = findKeys(column)
            count += 1

        # This creates a list for each column of data
        print(keyList)
        listgroup = [[] for j in range(len(keyList))]

        # give each key a list of it's underlying values (the value of each row in that column)
        for i in range(len(keyList)):
            keyvar = keyList[i]
            for k in range(count):
                listgroup[i].append(setList[k][keyvar])

            d = {keyvar: listgroup[i]}
            dicttwo.update(d)

        print(dicttwo)

    leafDict1 = {'leaves': longlist1}
    spineDict1 = {'spines': longlist2}
    leafPairsDict = {'leafpairs': longlist3}
    vlanDict = {'vlans': longlist4}
    domainDict = {'domains': longlist5}
    aepDict = {'aeps': longlist6}

    for k in range(len(dicttwo['nodeName'])):
        newDict1 = {}
        if (dicttwo['type'][k]) == "leaf":
            newDict1.update({"lname": dicttwo['nodeName'][k]})
            newDict1.update({"nodeid": int(dicttwo['nodeID'][k])})
            newDict1.update({"lserial": dicttwo['serialNum'][k]})
            newDict1.update({"mgmtAddress": dicttwo['mgmtAddress'][k]})
            newDict1.update({"mgmtGateway": dicttwo['mgmtGateway'][k]})
            newDict1.update({"lnodeto": int(dicttwo['nodeID'][k])})
            newDict1.update({"lnodefrom": int(dicttwo['nodeID'][k])})
            longlist1.append(newDict1)

    for k in range(len(dicttwo['nodeName'])):
        newDict2 = {}
        if (dicttwo['type'][k]) == "spine":
            newDict2.update({"sname": dicttwo['nodeName'][k]})
            newDict2.update({"nodeid": int(dicttwo['nodeID'][k])})
            newDict2.update({"sserial": dicttwo['serialNum'][k]})
            newDict2.update({"mgmtAddress": dicttwo['mgmtAddress'][k]})
            newDict2.update({"mgmtGateway": dicttwo['mgmtGateway'][k]})
            newDict2.update({"snodeto": int(dicttwo['nodeID'][k])})
            newDict2.update({"snodefrom": int(dicttwo['nodeID'][k])})
            longlist2.append(newDict2)

    for k in range(len(dicttwo['nodeName'])):
        newDict3 = {}
        if (dicttwo['type'][k]) == "vpc":
            newDict3.update({"lname": dicttwo['nodeName'][k]})
            newDict3.update({"lnodeto": int(dicttwo['nodeTo'][k])})
            newDict3.update({"lnodefrom": int(dicttwo['nodeFrom'][k])})
            newDict3.update({"vpcDomain": int(dicttwo['vpcDomain'][k])})
            longlist3.append(newDict3)

    for k in range(len(dicttwo['nodeName'])):
        newDict4 = {}
        if (dicttwo['vlPoolName'][k]) != "":
            newDict4.update({"poolname": dicttwo['vlPoolName'][k]})
            newDict4.update({"pooltype": dicttwo['poolType'][k]})
            newDict4.update({"encapallocmode": dicttwo['encapallocmode'][k]})
            newDict4.update({"encapstart": int(dicttwo['encapstart'][k])})
            newDict4.update({"encapend": int(dicttwo['encapend'][k])})
            longlist4.append(newDict4)

    for k in range(len(dicttwo['nodeName'])):
        newDict5 = {}
        if (dicttwo['domainName'][k]) != "":
            newDict5.update({"domainname": dicttwo['domainName'][k]})
            newDict5.update({"domaintype": dicttwo['domainType'][k]})
            newDict5.update({"vmmprovider": dicttwo['vmmProvider'][k]})
            newDict5.update({"vcenter": dicttwo['vcenter'][k]})
            newDict5.update({"datacenter": dicttwo['vcDataCenter'][k]})
            newDict5.update({"assocpool": dicttwo['vlPoolName'][k]})
            newDict5.update({"allocmode": dicttwo['encapallocmode'][k]})
            longlist5.append(newDict5)

    for k in range(len(dicttwo['nodeName'])):
        newDict6 = {}
        if (dicttwo['aepName'][k]) != "":
            newDict6.update({"aepname": dicttwo['aepName'][k]})
            newDict6.update({"assocdomain": dicttwo['domainName'][k]})
            newDict6.update({"domaintype": dicttwo['domainType'][k]})
            newDict6.update({"vmmprovider": dicttwo['vmmProvider'][k]})
            longlist6.append(newDict6)

    with open(outfile, 'w+') as yml_file:
        shove = yaml.dump(leafDict1, yml_file)
        shove = yaml.dump(spineDict1, yml_file)
        shove = yaml.dump(leafPairsDict, yml_file)
        shove = yaml.dump(vlanDict, yml_file)
        shove = yaml.dump(domainDict, yml_file)
        shove = yaml.dump(aepDict, yml_file)




# function to pull all the keys out (for creating lists for all of them and finding their values)
def findKeys(dict):
    return [*dict]


main()
