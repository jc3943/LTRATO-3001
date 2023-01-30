Tags = [{
    Key   = "DC"
    Value = "DAHL"
  },
  {
    Key   = "ENV"
    Value = "SANDBOX"
  }]

object_type = "https" # Options: https, cifs, nfs
enable_https = true
enable_cifs = false
enable_nfs = false

# create_os_repo
repo_name               = "ESXi-6.7"
repo_nr_version         = "ESXi 6.7 U3"
repo_vendor             = "VMware"
repo_description        = "ESXi 6.7 U3 Cisco Custom ISO"
repo_source_os_iso_path = "http://172.16.65.167/00-Software/ESX/VMware-ESXi-6.7.0-17700523-Custom-Cisco-6.7.3.1.iso"

# Common attributes between OS/SCU Resources:
repo_source_cifs_mount_options = ""
repo_source_nfs_mount_options  = ""
repo_source_user               = ""
repo_source_password           = ""

# create_scu_repo
repo_source_scu_iso_path = "http://172.16.65.167/00-Software/Intersight/ucs-cxxx-scu-6.1.3c.iso"
scu_name                 = "SCU-6.1.3c"
scu_description          = "SCU 6.1.3c software config utility"
scu_nr_version           = "6.1.3c"
scu_supported_models     = ["UCSC-C220-M5SX", "UCSC-C220-M5L", "UCSC-C220-M5SN", "HX220C-M5SX", "HXAF220C-M5SX", "C-series"]
