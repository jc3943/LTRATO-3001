# Jeff Comer (orig: Cal Donnelly) 
# take in a specifically formatted csv file and create a YAML file
# Section 1: bring in the csv and arrange the data by column in a list of dictionaries
# Section 2: fill a new dictionary with the reorganized list of dictionaries
# Section 3: Slap all the new data onto a fresh YAML file
# Sections are denoted by dash lines (---------)

import yaml
from yaml import *

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
    longlist = []
    overlist = []
    bigDict = {}
    dicttwo = {}
    dict3 = {}

    # open the CSV file and read it's contents to a list of dictionaries
    with open('port-defs.csv', 'r') as csv_file:
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

    newDict1 = {'Interface': longlist}

    for k in range(len(dicttwo['Interface'])):
        newDict2 = {}
        newDict2.update({"Interface": dicttwo['Interface'][k]})
        newDict2.update({"Description": dicttwo['Description'][k]})
        newDict2.update({"Speed": int(dicttwo['Speed'][k])})
        newDict2.update({"Mode": dicttwo['Mode'][k]})
        newDict2.update({"VLAN": int(dicttwo['VLAN'][k])})
        newDict2.update({"Type": dicttwo['Type'][k]})
        newDict2.update({"Enabled": str2bool(dicttwo['Enabled'][k])})
        longlist.append(newDict2)

    with open('nxos-ports.yaml', 'w+') as yml_file:
        shove = yaml.dump(newDict1, yml_file)



# function to pull all the keys out (for creating lists for all of them and finding their values)
def findKeys(dict):
    return [*dict]


main()
