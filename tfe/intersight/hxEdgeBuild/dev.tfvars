# Configure Environment-1 Specific variables 
# Intersight Access API Key
api_key                                     = "6273ddc07564612d30091b97/6273e4cc7564612d300964b9/62f53d6e7564612d30253ff4"
secret_key                                  = "../../../creds/qa-isight-SecretKey.txt"
endpoint                                    = "https://qa-intersight.thor.iws.navy.mil"
# Common
org_name                                    = "default"
# Tags
tag_key1                                    = "hx"
tag_value1                                  = "m5"

# auto_support_policy 
hx_auto_support_name                        = "sandbox-autoSupport"
hx_auto_support_description                 = "auto support policy"
hx_auto_support_service_ticket_receipient   = "thor@thor.iws.navy.mil"
hx_auto_support_admin_state                 = false

# cluster_network_policy
hx_network_policy_name                      = "sandbox-networPolicy"
hx_network_policy_description               = "Network Policy Definition"
hx_jumbo_frame                              = true
hx_uplink_speed                             = "10G"
hx_mgmt_vlan_name                           = "VLAN1200"
hx_mgmt_vlan_id                             = "1200"
## 10G options 
hx_vm_migration_vlan_name                   = "VLAN1202"
hx_vm_migration_vlan_id                     = "1202" # <int>
hx_vm_network_vlans_name                    = "VLAN1200"
hx_vm_network_vlans_id                      = "1200" # <int>
hx_mac_prefix_start_addr                    = "00:25:B5:AA"
hx_mac_prefix_end_addr                      = "00:25:B5:BB"

# cluster_storage_policy
hx_storage_policy_name                      = "sandbox-strPol"
hx_storage_policy_description               = "Storage policy for hx cluster"
hx_vdi_optimization                         = false
hx_disk_partition_cleanup                   = true
hx_logical_avalability_zone_config          = false

# local_credential_policy
hx_local_credential_policy_name             = "sandbox-localCreds"
hx_local_credential_policy_description      = "Local Credential Policy"
hx_factory_hypervisor_password              = true
hx_hxdp_root_pwd                            = "REVWUEBzc3cwcmQ="
hx_hypervisor_admin                         = "root"
hx_hypervisor_admin_pwd                     = "REVWUEBzc3cwcmQ="

# node_config_policy
node_config_policy_name                     = "sandbox-nodePol"
node_config_policy_description              = "Node Config Policy"
hx_node_name_prefix                         = "sandbox"

hx_hxdp_mgmt_start_addr                     = "172.16.114.11"
hx_hxdp_mgmt_end_addr                       = "172.16.114.13"
hx_hxdp_mgmt_gateway                        = "172.16.115.254"
hx_hxdp_mgmt_netmask                        = "255.255.252.0"

# hx_hxdp_data_start_addr                   = ""
# hx_hxdp_data_end_addr                     = ""
# hx_hxdp_data_gateway                      = ""
# hx_hxdp_data_netmask                      = ""

hx_hypervisor_mgmt_start_addr               = "172.16.115.11"
hx_hypervisor_mgmt_end_addr                 = "172.16.115.13"
hx_hypervisor_mgmt_gateway                  = "172.16.115.254"
hx_hypervisor_mgmt_netmask                  = "255.255.240.0"

hx_hypervisor_vmotion_start_addr            = "172.16.116.11"    
hx_hypervisor_vmotion_end_addr              = "172.16.116.13"  
hx_hypervisor_vmotion_gateway               = "172.16.116.254" 
hx_hypervisor_vmotion_netmask               = "255.255.255.0" 
hx_hypervisor_admin_user                    = "root"

# software_version_policy
hx_software_version_policy_name             = "sandbox-swVerPol"
hx_software_version_policy_description      = "Software Version Policy"
hx_hxdp_version                             = "4.5(2b)"

# sys_config_policy
hx_sys_config_policy_name                   = "sandbox-sysConfgi"
hx_sys_config_policy_description            = "System Config Policy"
hx_dns_domain_name                          = "thor.iws.navy.mil"
hx_dns_servers                              = ["172.16.20.101"] # ["x.x.x.1", "x.x.x.2"]
hx_ntp_servers                              = ["172.20.1.254"] # ["x.x.x.3", "x.x.x.4"]
hx_timezone                                 = "America/New_York"

# hx_proxy_setting_policy
# hx_proxy_policy_name                      = ""
# hx_proxy_policy_description               = ""
hx_proxy_username                           = "admin"
hx_proxy_password                           = "password"
hx_proxy_port                               = "80"
hx_proxy_ip                                 = "172.172.172.172"

# vcenter_config_policy 
hx_vcenter_config_policy_name               = "sandbox-vcenterPol"
hx_vcenter_config_policy_description        = "vCenter Config Policy"
hx_vcenter_dc_name                          = "sandbox"
hx_vcenter_ip                               = "172.16.14.137"
hx_vcenter_password                         = "REVWUEBzc3cwcmQ="
hx_vcenter_username                         = "administrator@vsphere.local"


## Replication_network_policy
# hx_replication_network_policy_name        = ""
# hx_replication_network_policy_description = ""
hx_replication_bandwidth_mbps               = "10000"
hx_replication_mtu                          = "1500" # <int>
hx_replication_vlan_name                    = "VLAN1205"
hx_replication_vlad_id                      = "1205"
hx_replication_ip_start_addr                = "172.16.117.1"
hx_replication_ip_end_addr                  = "172.16.117.10"
hx_replication_netmask                      = "255.255.255.0"
hx_replication_gateway                      = "172.16.117.254"

## Ext iSCSI Policy 
# hx_ext_iscsi_policy_name                  = ""
# hx_ext_iscsi_policy_description           = ""
hx_ext_iscsi_admin_state                    = false
hx_iscsi_exta_name                          = "VLAN1"
hx_iscsi_exta_vlan_id                       = 1
hx_iscsi_extb_name                          = "VLAN1"
hx_iscsi_extb_vlan_id                       = 1

## Ext FC storage policy
#hx_fc_storage_policy_name                  = ""
#hx_fc_storage_policy_description           = ""
#hx_fc_admin_state                          = "" # bool
hx_fc_exta_vsan_name                        = "VSAN1"
hx_fc_exta_vsan_id                          = "1" # <int>
hx_fc_extb_vsan_name                        = "VSAN1"
hx_fc_extb_vsan_id                          = "1" # <int>
hx_fc_wwxn_prefix_start_addr                = "20:00:00:25:B5:AA"
hx_fc_wwxn_prefix_end_addr                  = "20:00:00:25:B5:EF"
hx_fc_admin_state                           = false # bool

# cluster_profile
hx_profile_name                             = "sandbox-hxProfile"
hx_profile_description                      = "HX Cluster Profile"
cluster_name                                = "sandbox"
hx_host_name_prefix                         = "sandbox"
hx_data_ip_address                          = "169.254.1.1"
hx_hypervisor_type                          = "ESXi"
hx_mac_address_prefix                       = "00:25:B5:EF"
hx_mgmt_ip_address                          = "172.16.114.10"
hx_mgmt_platform                            = "EDGE"
hx_replication                              = "3"# <int>
hx_storage_data_vlan_name                   = "VLAN1201"
hx_storage_data_vlan_id                     = "1201" # <int>

# Server Names
server_names = [
  {
    name = "sandbox-01",
    hostname = "sandbox-01"
  },
  {
    name = "sandbox-02",
    hostname = "sandbox-02"
  },
  {
    name = "sandbox-03",
    hostname = "sandbox-01"
  }
]