#!/bin python
# Jeff Comer
# script to take in a csv seed file and convert to yaml
# example input csv is vars/<branch>/tenants.csv
# old, needs re-written using dictionaries for efficiency
"""
"""

import csv, sys, getopt

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
      print('create_yaml_from_csv_v4.1.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('create_yaml_from_csv_v4.1.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

    yaml = open(outputfile, "w")
    brdom = []
    dfgw = []
    subnetmask =[]
    tenant = []
    vrf = []
    app_profile = []
    description = []
    epg_name = []
    domain = []
    domainType = []
    contract = []
    encaps = []
    encaptype = []
    filter = []
    L3Out = []
    multivrf = []
    rp = []
    dhcpRelay = []
    dhcpProviderIP = []
    i = 0
    with open(inputfile) as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       next(csv_reader)
       for row in csv_reader:
         brdom.append(row[0])
         dfgw.append(row[1])
         subnetmask.append(row[2])
         tenant.append(row[3])
         vrf.append(row[4])
         app_profile.append(row[5])
         description.append(row[6])
         epg_name.append(row[7])
         domain.append(row[8])
         domainType.append(row[9])
         contract.append(row[10])
         encaps.append(row[11])
         encaptype.append(row[12])
         filter.append(row[13])
         L3Out.append(row[14])
         multivrf.append(row[15])
         rp.append(row[16])
         dhcpRelay.append(row[17])
         dhcpProviderIP.append(row[18])
         row_count = i
         i = i + 1
       u_tenant_list = []
       for x in tenant:
         if x not in u_tenant_list :
           u_tenant_list.append(x)
       yaml.write("tenants:\n")
       for x in u_tenant_list:
         yaml.write("  - tenant: " + x + "\n")
       u_vrf_list = []
       vrftenant = []
       for x,y in zip(vrf, tenant):
         if x not in u_vrf_list:
           u_vrf_list.append(x)
           vrftenant.append(y)
       yaml.write("vrfs:\n")
       for x, y, z in zip(u_vrf_list, vrftenant, rp):
         yaml.write("  - vrf: " + x + "\n")          
         yaml.write("    tenant: " + y + "\n")
         yaml.write("    rp: " + z + "\n")
       u_ap_list = []
       aptenant = []
       for x,y in zip(app_profile, tenant):
         if x not in u_ap_list:
           u_ap_list.append(x)
           aptenant.append(y)
       yaml.write("aps:\n")
       for x, y in zip(u_ap_list, aptenant):
         yaml.write("  - ap: " + x + "\n")
         yaml.write("    tenant: " + y + "\n")
       yaml.write("bridge_domains:\n")
       for v, w, x, y, z, zz, aa, bb in zip(tenant, vrf, brdom, dfgw, subnetmask, L3Out, dhcpRelay, dhcpProviderIP):
         yaml.write("  - bd: " + x + "\n")
         yaml.write("    gateway: " + y + "\n")
         yaml.write("    mask: " + z + "\n")
         yaml.write("    tenant: " + v + "\n")
         yaml.write("    vrf: " + w + "\n")
         yaml.write("    scope: public,shared" + "\n")
         yaml.write("    L3Out: " + zz + "\n")
         yaml.write("    dhcpRelay: " + aa + "\n")
         yaml.write("    dhcpProviderIP: " + bb + "\n")
       yaml.write("epgs:\n")
       for a, b, c, d, u, v, w, x, y, yy, z, zz in zip(dfgw, subnetmask, description, multivrf, tenant, app_profile, epg_name, brdom, domain, domainType, encaps, encaptype):
         yaml.write("  - epg: " + w + "\n")
         yaml.write("    tenant: " + u + "\n")
         yaml.write("    ap: " + v + "\n")
         yaml.write("    bd: " + x + "\n")
         yaml.write("    domain: " + y + "\n")
         yaml.write("    domainType: " + yy + "\n")
         yaml.write("    encaps: " + z + "\n")
         yaml.write("    encaptype: " + zz + "\n")
         yaml.write("    gateway: " + a + "\n")
         yaml.write("    mask: " + b + "\n")
         yaml.write("    description: " + c + "\n")
         yaml.write("    multivrf: " + d + "\n")
       yaml.write("epg_contracts:\n")
       for w, x, y, z in zip(tenant, epg_name, contract, app_profile):
         yaml.write("  - epg: " + x + "\n")
         yaml.write("    contract: " + y + "\n")
         yaml.write("    contract_type: \"provider\"\n")
         yaml.write("    ap: " + z + "\n")
         yaml.write("    tenant: " + w + "\n")
         yaml.write("  - epg: " + x + "\n")
         yaml.write("    contract: " + y + "\n")
         yaml.write("    contract_type: \"consumer\"\n")
         yaml.write("    ap: " + z + "\n")
         yaml.write("    tenant: " + w + "\n")
       u_contract_list = []
       contract_tenant = []
       contract_filter = []
       for x, y, z in zip(contract, tenant, filter):
         if x not in u_contract_list:
           u_contract_list.append(x)
           contract_tenant.append(y)
           contract_filter.append(z)
       yaml.write("contracts:\n")
       for x, y, z in zip(u_contract_list, contract_tenant, contract_filter):
         yaml.write("  - contract: " + x + "\n")
         yaml.write("    tenant: " + y + "\n")
         yaml.write("    subject: \"Subject\"\n")
         yaml.write("    filter: " + z + "\n")
       u_filter_list = []
       filter_tenant = []
       for x, y in zip(filter, tenant):
         if x not in u_filter_list:
           u_filter_list.append(x)
           filter_tenant.append(y)
       yaml.write("filters:\n")
       for x, y in zip(u_filter_list, filter_tenant):
         yaml.write("  - filter: " + x + "\n")
         yaml.write("    tenant: " + y + "\n")
         yaml.write("    entry: \"default\"\n")
         yaml.write("    ethertype: \"unspecified\"\n")
    csv_file.close()
    yaml.close()

if __name__ == '__main__':
    main(sys.argv[1:])
