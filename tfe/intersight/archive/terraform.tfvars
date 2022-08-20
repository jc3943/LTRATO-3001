# Modify the following example variables with valid settings for the HX cluster you wish to deploy

# API access
api_key = "6273ddc07564612d30091b97/6273e4cc7564612d300964b9/62f53d6e7564612d30253ff4"
api_key_file = "../../../creds/qa-isight-SecretKey.txt"
api_endpoint = "https://qa-intersight.thor.iws.navy.mil"

# Hyperflex Cluster
cluster_name = "dev-hx-m4"
disk_cleanup = "false"
vdi_opt = "false"
organization = "default"

# Management Platform, enter "FI" for standard or "EDGE" for Edge
management_platform = "EDGE"

# Network Policies
jumbo_frame = "true"
uplink_speed = "10G"

# HX Management IP
mgmt_vlan_id = "1200"
hx_mgmt_ip = "172.16.114.10"
hx_ip_start = "172.16.114.11"
hx_ip_end = "172.16.114.13"
hx_netmask = "255.255.240.0"
hx_gateway = "172.16.115.254"

# MAC prefix
mac_prefix = "00:25:B5:AA"

# WWXN prefix
wwxn_prefix = ""

# Storage VLAN
storage_vlan_id = "1201"

# HXDP Version
hxdp_version = "4.0(2d)"

# HX password
#hx_password = ""

# ESXi admin account
esx_admin = "root"

# ESXi admin password
#esx_password = ""

# ESXi Management IP
node_prefix = "dev-hx-m4"
mgmt_ip_start = "172.16.115.11"
mgmt_ip_end = "172.16.115.11"
mgmt_netmask = "255.255.240.0"
mgmt_gateway = "172.16.115.254"

# Time
timezone = "America/Chicago"
ntp = ["172.20.1.254"]

# DNS
dns_domain = "thor.iws.navy.mil"
dns = ["172.16.20.101"]

# VCenter
vcenter_hostname = "hx-dev-vcsa.thor.iws.navy.mi"
vcenter_username = "administrator@vsphere.local"
#vcenter_password = ""
vcenter_datacenter = "HX_DEV" 

# iSCSI Additional vNICs
additional_vNICs = "false"
iscsi_vlan_a_name = ""
iscsi_vlan_a_id = "0"
iscsi_vlan_b_name = ""
iscsi_vlan_b_id = "0"

# FC Additional vHBAs
additional_vHBAs = "false"
fc_vsan_a_name = ""
fc_vsan_a_id = "0"
fc_vsan_b_name = ""
fc_vsan_b_id = "0"
fc_wwxn_range_start = ""
fc_wwxn_range_end = ""

# Auto Support
auto_support_enable = "false"
auto_support_recipient = ""

# Proxy Server
proxy_enable = "false"
proxy_hostname = ""
proxy_port = "80"

# Server Names
server_names = [
  {
    name = "dev-hx-m4-01",
    hostname = "dev-hx-m4-01"
  },
  {
    name = "dev-hx-m4-02",
    hostname = "dev-hx-m4-02"
  },
  {
    name = "dev-hx-m4-03",
    hostname = "dev-hx-m4-01"
  }
]