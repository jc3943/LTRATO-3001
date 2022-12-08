# Callaghan Donnelly
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
    with open('vars/bh-prod/aci/port-defs.csv', 'r') as csv_file:
        csvread = csv.DictReader(csv_file)
        for column in csvread:
            # append each dict to the list
            setList.append(column)
            # make a list of keys (in this case it is all the columns)
            if count == 0:
                keyList = findKeys(column)
            count += 1

        # This creates a list for each column of data
    #    print(keyList)
        listgroup = [[] for j in range(len(keyList))]

        # give each key a list of it's underlying values (the value of each row in that column)
        for i in range(len(keyList)):
            keyvar = keyList[i]
            for k in range(count):
                listgroup[i].append(setList[k][keyvar])

            d = {keyvar: listgroup[i]}
            dicttwo.update(d)

#     print(dicttwo)

    # -----------------------------------------------------------------
    # newDict1 is the dictionary that stores all of the info, newDict2 is the dictionary that is used to format the info as it is created
    newDict1 = {'policyGrps': longlist}

    # find if and where there are repeated entries, so that they won't get repeated in policyGrps
    for k in range(len(dicttwo['name'])):
        try:
            newspot = dicttwo['name'][k+1]
        except IndexError:
            newspot = 'null'

        if dicttwo['name'][k] == newspot:
            overlist.append(newspot)

#        print(overlist)

    # for every interaction that is given in the sheet, run the stuff
    for q in range(len(dicttwo['interactions'])):
        # if the interaction we are looking at is policyGrps
        if dicttwo['interactions'][q] == 'policyGrps':
            # for every row within the sheet
            for k in range(len(dicttwo['name'])):
                # only run if it is not a duplicate of another item
                if dicttwo['name'][k] not in overlist:
                    # clear newDict2 every time we run so it can be reused
                    newDict2 = {}
                    # add each item with it's corresponding element for this item(row)
                    newDict2.update({"name": dicttwo['name'][k]})
                    newDict2.update({"speed": dicttwo['speed'][k]})

                    if dicttwo['intfType'][k] == "vpc":
                        newDict2.update({"lagType": "node"})

                    elif dicttwo['intfType'][k] == "access":
                        newDict2.update({"lagType": "leaf"})

                    newDict2.update({"cdpPol": dicttwo['cdpPol'][k]})
                    newDict2.update({"lldpPol": dicttwo['lldpPol'][k]})
                    newDict2.update({"mcpPol": dicttwo['mcpPol'][k]})
                    newDict2.update({"monPol": dicttwo['monPol'][k]})
                    newDict2.update({"stormCtlPol": dicttwo['stormCtlPol'][k]})
                    newDict2.update({"lacpPol": dicttwo['lacpPol'][k]})
                    newDict2.update({"aep": dicttwo['aep'][k]})

                    # add this row to the list so we can clear the dictionary for the next run
                    longlist.append(newDict2)
                # if it is a duplicate, then clear it out, and allow only the original to be output
                if dicttwo['name'][k] in overlist:
                    rid = dicttwo['name'][k]
                    overlist.remove(rid)


        # if the interaction we are dealing with is interfaceProfiles
        elif dicttwo['interactions'][q] == 'interfaceProfiles':
            # create and add a list to the overall dictionary
            newlist = []
            setin = {'interfaceProfiles': newlist}
            newDict1.update(setin)
            # again, run for every item in the sheet
            for k in range(len(dicttwo['name'])):
                newDict2 = {}
                newDict2.update({"name": dicttwo['name'][k]})
                newDict2.update({"description": dicttwo['description'][k]})
                newDict2.update({"interfaceProfile": dicttwo['interfaceProfile'][k]})
                newDict2.update({"policyGrp": dicttwo['name'][k]})
                newDict2.update({"blkNum": dicttwo['blkNum'][k]})

                if dicttwo['intfType'][k] == "vpc":
                    newDict2.update({"intfType": "vpc"})

                elif dicttwo['intfType'][k] == "access":
                    newDict2.update({"intfType": "switch_port"})

                fromPort = dicttwo['fromPort'][k]
                toPort = dicttwo['toPort'][k]
                newDict2.update({"fromPort": int(fromPort)})
                newDict2.update({"toPort": int(toPort)})

                newlist.append(newDict2)


    # -------------------------------------------------------------------------

    # print(newDict1)

    # print all of the key : value pairs to the yaml file
    with open('vars/bh-prod/aci/aci-ports.yaml', 'w+') as yml_file:
        shove = yaml.dump(newDict1, yml_file)

    # print("Success!")

# function to pull all the keys out (for creating lists for all of them and finding their values)
def findKeys(dict):
    return [*dict]


main()
