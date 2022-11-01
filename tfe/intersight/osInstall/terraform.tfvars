# Intersight Access API Key
api_key    = "6273ddc07564612d30091b97/6273e4cc7564612d300964b9/62f53d6e7564612d30253ff4"
secret_key = "../../../creds/qa-isight-SecretKey.txt"
endpoint   = "https://qa-intersight.thor.iws.navy.mil"

org_name   = "default"

# Common
# Tags
tags = {
  key1   = "DC"
  value1 = "DAHL"
  key2   = "ENV"
  value2 = "SANDBOX"
}

# create_os_repo  
repo_name               = "ESXi-6.7"
repo_nr_version         = "ESXi 6.7 U3"
repo_vendor             = "VMware"
repo_description        = "ESXi 6.7 U3 Cisco Custom ISO" # # Options: check Intersight GUI     = "ESXi 6.7 U3 Cisco Custom ISO"
repo_source_os_iso_path = "http://172.16.65.167/00-Software/ESX/VMware-ESXi-6.7.0-17700523-Custom-Cisco-6.7.3.1.iso"

# Common attributes between OS/SCU Resources: 
repo_source_object_type        = "softwarerepository.HttpServer" # softwarerepository.HttpServer, softwarerepository.CifsServer, softwarerepository.NfsServer
repo_source_cifs_mount_options = ""
repo_source_nfs_mount_options  = ""
repo_source_user               = ""
repo_source_password           = ""

# create_scu_repo 
repo_source_scu_iso_path = "http://172.16.65.167/00-Software/Intersight/ucs-cxxx-scu-6.1.3c.iso"
scu_name                 = "SCU-6.1.3c"
scu_description          = ""
scu_nr_version           = "6.1.3c"
scu_supported_models     = ["C-series", ]

# os_install
os_install_server_selector             = "$filter=Serial eq 'WMP2443017J'"
os_install_configuration_file_selector = "$filter=Name eq 'esxi-cfg-kst'"
# Configuration Source : Cisco 
# Configuration File : 
# ESXi  : ESXi6.7ConfigFile, ESXi6.5ConfigFile, 
# Redhat: RHEL8ConfigFile, RHEL7ConfigFile
# Ubuntu: No cisco provided config
# Windows: Windows2019ConfigFile, Windows2016ConfigFile
os_hostname       = "sandbox-exsi-bm"
os_ip_config_type = "static"

## OS IP Info
os_ipv4_addr         = "172.16.115.41"
os_ipv4_netmask      = "255.255.252.0"
os_ipv4_gateway      = "172.16.115.254"
os_ipv4_dns_ip       = "172.16.20.101"
os_root_password     = "DEVP@ssw0rd"
os_answers_nr_source = "Template" # Template for cisco provided source files

## os_tmpl_file
os_tmpl_name         = "sandbox-esxi"
os_tmpl_file    = "../../../vmware/sandbox-esxi-bm.csv"

