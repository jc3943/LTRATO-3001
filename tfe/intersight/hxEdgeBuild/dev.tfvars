# Please update the values as per your environment. 
# Intersight Access API Key
api_key                                     = "<api_key>"
secret_key                                  = "<Secret_key_file"
endpoint                                    = "https://intersight.com"

# Org Details
org_name                                    = "default"

# Cluster Info
cluster_name                                = "tf_hx_edge_sj"

# Common
# Tags
tag_key1                                    = "ENV"
tag_value1                                  = "LAB"

# auto_support_policy 
hx_auto_support_service_ticket_receipient   = "lab@lab.com"
hx_auto_support_admin_state                 = "false" # <bool>

# cluster_network_policy
hx_jumbo_frame                              = true # <bool>
hx_uplink_speed                             = "1G" # 10G
hx_mgmt_vlan_name                           = "mgmt_vlan"
hx_mgmt_vlan_id                             = 101 # <int>
## 10G Options
hx_mac_prefix_start_addr                    = "00:25:B5:00"
hx_mac_prefix_end_addr                      = "00:25:B5:01"
hx_vm_migration_vlan_name                   = "vmotion_vlan"
hx_vm_migration_vlan_id                     = 20 # <int>
hx_vm_network_vlans_name                    = "vm_vlanx"
hx_vm_network_vlans_id                      = 50 # <int>


# cluster_storage_policy
hx_vdi_optimization                         = "true" # <bool>
hx_disk_partition_cleanup                   = "true" # <bool>
hx_logical_avalability_zone_config          = "false" # <bool>

# local_credential_policy
hx_factory_hypervisor_password              = "true" # bool
hx_hxdp_root_pwd                            = "C1sco12345!"
hx_hypervisor_admin_user                    = "root"
hx_hypervisor_admin_pwd                     = "C1sco12345!"

# node_config_policy
hx_node_name_prefix                         = "lab-edge"
## Hypervisor mgmt/vmk0 IP range
hx_hypervisor_mgmt_start_addr               = "10.1.0.21"
hx_hypervisor_mgmt_end_addr                 = "10.1.0.30"
hx_hypervisor_mgmt_gateway                  = "10.1.0.1"
hx_hypervisor_mgmt_netmask                  = "255.255.255.0"
## hxdp mgmt/eth0 IP range 
hx_hxdp_mgmt_start_addr                     = "10.1.0.2"
hx_hxdp_mgmt_end_addr                       = "10.1.0.10"
hx_hxdp_mgmt_gateway                        = "10.1.0.1"
hx_hxdp_mgmt_netmask                        = "255.255.255.0"
## hxdp data/eth1 IP range
# hx_hxdp_data_start_addr                   = ""
# hx_hxdp_data_end_addr                     = ""
# hx_hxdp_data_gateway                      = ""
# hx_hxdp_data_netmask                      = ""
## Hypervisor vMotion IP range
# hx_hypervisor_vmotion_start_addr            = "10.3.0.21"
# hx_hypervisor_vmotion_end_addr              = "10.3.0.30"
# hx_hypervisor_vmotion_gateway               = "10.3.0.1"
# hx_hypervisor_vmotion_netmask               = "255.255.255.0"

# software_version_policy
hx_hxdp_version                             = "4.0(2c)"

# sys_config_policy
hx_dns_domain_name                          = "lab.lab"
hx_dns_servers                              = ["1.1.1.1", "2.2.2.2"] # ["x.x.x.1", "x.x.x.2"]
hx_ntp_servers                              = ["11.11.11.11", "22.22.22.22"] # ["x.x.x.3", "x.x.x.4"]
hx_timezone                                 = "America/Los_Angeles"

# hx_proxy_setting_policy
hx_proxy_username                           = ""
hx_proxy_password                           = ""
hx_proxy_port                               = 8080
hx_proxy_ip                                 = "1.1.1.1"

# vcenter_config_policy 
hx_vcenter_dc_name                          = "lab-dc"
hx_vcenter_ip                               = "10.1.1.1"
hx_vcenter_password                         = "C1sco12345!"
hx_vcenter_username                         = "administrator@vsphere.local"

# Replication_network_policy
hx_replication_bandwidth_mbps             = 1000
hx_replication_mtu                        = 1500 # <int>
hx_replication_vlan_name                  = "replication_vlan"
hx_replication_vlad_id                    = 14  # <int> 
hx_replication_ip_start_addr              = ""
hx_replication_ip_end_addr                = ""
hx_replication_netmask                    = ""
hx_replication_gateway                    = ""

# Ext iSCSI Policy 
hx_ext_iscsi_admin_state                  = "false" # bool
hx_iscsi_exta_name                        = "iscsi_vlan_a"
hx_iscsi_exta_vlan_id                     = 14 # <int>
hx_iscsi_extb_name                        = "iscsi_vlan_b"
hx_iscsi_extb_vlan_id                     = 15 # <int>

# Ext FC storage policy
hx_fc_admin_state                          = "false" # bool
hx_fc_exta_vsan_name                       = "vsan_a"
hx_fc_exta_vsan_id                         = 14 # <int>
hx_fc_extb_vsan_name                       = "vsan_b"
hx_fc_extb_vsan_id                         = 15 # <int>
hx_fc_wwxn_prefix_start_addr               = "20:00:00:25:B5:00"
hx_fc_wwxn_prefix_end_addr                 = "20:00:00:25:B5:FF"

# cluster_profile
hx_data_ip_address                          = "10.0.1.2"
hx_hypervisor_type                          = "ESXi"
hx_mac_address_prefix                       = "00:25:B5:AB"
hx_mgmt_ip_address                          = "10.1.0.11"
hx_mgmt_platform                            = "EDGE"
hx_replication                              = 2 # <int>
hx_storage_data_vlan_name                   = "lab-storage-vlan"
hx_storage_data_vlan_id                     = 102 # <int>
hx_host_name_prefix                         = "hx-sj"

# node_config_policy
hx_servers = {
    server1_serial = ""
    server2_serial = ""
}