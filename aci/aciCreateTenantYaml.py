#!/bin python
# Jeff Comer
# script to take in a csv seed file and convert to yaml
# example input csv is vars/<branch>/tenants.csv
# old, needs re-written using dictionaries for efficiency
"""
"""

import csv, sys, getopt, os, yaml

def main(argv):
    """
    Main execution routine

    :return: None
    """

    inputfile = ''
    outputfile = ''
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print('aciCreateTenantYaml.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('aciCreateTenantYaml.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

if __name__ == '__main__':
    cliArgs = main(sys.argv[1:])