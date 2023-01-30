# Intersight Access API Key
# Common
org_name = "default"
server_serial = "WMP2443017J"
os_config_file = "ESXi6.7ConfigFile"

os_repo_name = "ESXi-6.7"
scu_repo_name = "SCU-6.1.3c"

# os_install
# Configuration Source : Cisco
# Configuration File :
# ESXi  : ESXi6.7ConfigFile, ESXi6.5ConfigFile,
# Redhat: RHEL8ConfigFile, RHEL7ConfigFile
# Ubuntu: No cisco provided config
# Windows: Windows2019ConfigFile, Windows2016ConfigFile
os_hostname       = "sandbox-bm-esxi.thor.iws.nayv.mil"
os_ip_config_type = "static"

## OS IP Info
os_ipv4_addr         = "172.16.115.41"
os_ipv4_netmask      = "255.255.252.0"
os_ipv4_gateway      = "172.16.115.254"
os_ipv4_dns_ip       = "172.16.20.101"
os_root_password     = "DEVP@ssw0rd"
os_answers_nr_source = "Template" # Template for cisco provided source files
os_answers_netDev    = "vmnic5"
os_answers_vlanId    = 1200
