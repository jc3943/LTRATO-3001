# Configure Default variables in this file
# Intersight Access API Key
variable "api_key" {
  type        = string
  description = "Intersight API key"
}

variable "secret_key" {
  type        = string
  description = "Intersight Secret Key file"
}

variable "endpoint" {
  type        = string
  description = "Intersight URL"
}

# Org Details
variable "org_name" {
  type        = string
  description = "Name of the Org where you want to create the resource"
}

# Cluster Info 
variable "cluster_name" {
  type        = string
  description = "Name of the Cluster"
}
variable "hx_profile_action" {
  type        = string
  description = "HX Profile action: validation/deploy, etc"
  default     = "validate" # Validate, Deploy 
}

# Common
# Tags
variable "tag_key1" {
  type        = string
  description = "Environment Specific tag name"
}
variable "tag_value1" {
  type        = string
  description = "Environment Specific tag value"
}


# auto_support_policy OPTIONAL 
variable "hx_auto_support_service_ticket_receipient" {
  type        = string
  description = "Auto Support receipient email ID"
}
variable "hx_auto_support_admin_state" {
  type        = bool
  description = "Enable or disable Auto Support"
}

# network_config_policy
variable "hx_jumbo_frame" {
  type        = bool
  description = "Enable or disable jumbo frames"
}
variable "hx_uplink_speed" {
  type        = string
  description = "Uplink speed, possible values: 1G or 10G"
}
### mgmt_vlan (Type: HashMap)
variable "hx_mgmt_vlan_id" {
  type        = number
  description = "mgmt VLAN id, the mgmt VLAN must have outbound network connectivity to Intersight"
}

## 10G options 
## MAC address prefix range for configuring vNICs
### mac_prefix_range (Type: HashMap)
variable "hx_mac_prefix_start_addr" {
  type        = string
  description = "vNIC mac address range start"
}
variable "hx_mac_prefix_end_addr" {
  type        = string
  description = "vNIC mac address range end"
}
## Mgmt vlan name 
### mgmt_vlan (Type: HashMap)
variable "hx_mgmt_vlan_name" {
  type        = string
  description = "hx mgmt vlan name"
}
### vm_migration_vlan (Type: HashMap)
variable "hx_vm_migration_vlan_name" {
  type        = string
  description = "VM migration/vMotion VLAN name"
}
variable "hx_vm_migration_vlan_id" {
  type        = number
  description = "VM migration/vMotion VLAN id"
}
### vm_network_vlans (Type: Array)
variable "hx_vm_network_vlans_name" {
  type        = string
  description = "VM Network vlan name"
}
variable "hx_vm_network_vlans_id" {
  type        = number
  description = "VM Network vlan id"
}
## Out-of-band KVM IP range 
### kvm_ip_range Type (Type: HashMap)
/*
variable "hx_kvm_oob_start_addr" {
  type        = string
  description = "Out of band range start ip"
}
variable "hx_kvm_oob_end_addr" {
  type        = string
  description = "Out of band range end ip"
}
variable "hx_kvm_oob_netmask" {
  type        = string
  description = "Out of band range netmask"
}
variable "hx_kvm_oob_gateway" {
  type        = string
  description = "Out of band range gateway"
}
*/
# cluster_storage_policy OPTIONAL
variable "hx_vdi_optimization" {
  type        = bool
  description = "Enable or disable VDI optimization (hybrid HyperFlex systems only)"
}
variable "hx_disk_partition_cleanup" {
  type        = bool
  description = "If enabled, formats existing disk partitions (destroys all user data)."
}
###   logical_avalability_zone_config  Type: (hashmap)
variable "hx_logical_avalability_zone_config" {
  type        = bool
  description = "Enable or disable Logical Availability Zones (LAZ)"
}


# local_credential_policy : Security Policy
variable "hx_factory_hypervisor_password" {
  type        = bool
  description = "Indicates if Hypervisor password is the factory set default password. "
}
variable "hx_hypervisor_admin_user" {
  type        = string
  description = "Hypervisor administrator username"
}
variable "hx_hypervisor_admin_pwd" {
  type        = string
  description = "Hypervisor administrator password"
}
variable "hx_hxdp_root_pwd" {
  type        = string
  description = "HyperFlex storage controller VM password"
}

# node_config_policy
variable "hx_node_name_prefix" {
  type        = string
  description = "used to automatically generate the default hostname for each server."
}

## Hypervisor mgmt/vmk0 IP range
variable "hx_hypervisor_mgmt_start_addr" {
  type        = string
  description = "Hypervisor Mgmt/vmk0 start IP"
}
variable "hx_hypervisor_mgmt_end_addr" {
  type        = string
  description = "Hypervisor Mgmt/vmk0 end IP"
}
variable "hx_hypervisor_mgmt_gateway" {
  type        = string
  description = "Hypervisor Mgmt/vmk0 Gateway"
}
variable "hx_hypervisor_mgmt_netmask" {
  type        = string
  description = "Hypervisor Mgmt/vmk0 Netmask"
}

## hxdp mgmt/eth0 IP range 
variable "hx_hxdp_mgmt_start_addr" {
  type        = string
  description = "CtrlVM management/eth0 start IP"
}
variable "hx_hxdp_mgmt_end_addr" {
  type        = string
  description = "CtrlVM management/eth0 end IP"
}
variable "hx_hxdp_mgmt_gateway" {
  type        = string
  description = "CtrlVM management/eth0 Gateway"
}
variable "hx_hxdp_mgmt_netmask" {
  type        = string
  description = "CtrlVM management/eth0 Netmask"
}

## hxdp data/eth1 IP range
# variable "hx_hxdp_data_start_addr" {
#   type        = string
#   description = "CtrlVM Data/eth1 start IP"
# }
# variable "hx_hxdp_data_end_addr" {
#   type        = string
#   description = "CtrlVM Data/eth1 end IP"
# }
# variable "hx_hxdp_data_gateway" {
#   type        = string
#   description = "CtrlVM Data/eth1 Gateway"
# }
# variable "hx_hxdp_data_netmask" {
#   type        = string
#   description = "CtrlVM Data/eth1 Netmask"
# }
#
## Hypervisor vMotion IP range
# variable "hx_hypervisor_vmotion_start_addr" {
#   type        = string
#   description = "Hypervisor vmotion start IP"
# }
# variable "hx_hypervisor_vmotion_end_addr" {
#   type        = string
#   description = "Hypervisor vmotion end IP"
# }
# variable "hx_hypervisor_vmotion_gateway" {
#   type        = string
#   description = "Hypervisor vmotion Gateway"
# }
# variable "hx_hypervisor_vmotion_netmask" {
#   type        = string
#   description = "Hypervisor vmotion Netmask"
# }


# software_version_policy
variable "hx_hxdp_version" {
  type        = string
  description = "Desired HXDP software version to apply on the HyperFlex cluster"
}

# sys_config_policy
variable "hx_dns_domain_name" {
  type        = string
  description = "The DNS Search Domain Name"
}
variable "hx_dns_servers" {
  type        = list(string)
  description = "list of DNS server IPs"
}
variable "hx_ntp_servers" {
  type        = list(string)
  description = "List of ntp server IPs"
}
variable "hx_timezone" {
  type        = string
  description = "Timezone"
  # Get the values from url: 
  # https://registry.terraform.io/providers/CiscoDevNet/intersight/latest/docs/resources/hyperflex_sys_config_policy
}

# proxy_setting_policy OPTIONAL
variable "hx_proxy_ip" {
  type        = string
  description = "HTTP Proxy server FQDN or IP."
}
variable "hx_proxy_password" {
  type        = string
  description = "The password for the HTTP Proxy"
}
variable "hx_proxy_port" {
  type        = number
  description = "The HTTP Proxy port number"
}
variable "hx_proxy_username" {
  type        = string
  description = "The username for the HTTP Proxy"
}


# vcenter_config_policy OPTIONAL
variable "hx_vcenter_dc_name" {
  type        = string
  description = "vCenter Datacenter Name"
}
variable "hx_vcenter_ip" {
  type        = string
  description = "vCenter Server FQDN or IP"
}
variable "hx_vcenter_username" {
  type        = string
  description = "vCenter Username"
}
variable "hx_vcenter_password" {
  type        = string
  description = "vCenter Password"
}

# Replication_network_policy
variable "hx_replication_bandwidth_mbps" {
  type        = string
  description = "Bandwidth for the Replication network in Mbps, range: 0-100000"
}
variable "hx_replication_mtu" {
  type        = number
  description = "MTU for the Replication network, range: 1024-1500"
}

##replication_vlan : Type:(hashmap)
variable "hx_replication_vlan_name" {
  type        = string
  description = "Replication Network VLAN Name"
}
variable "hx_replication_vlad_id" {
  type        = number
  description = "Replication Network VLAN Id, The management VLAN must have outbound network connectivity to Intersight, range: 0-4095"
}
## replication_ipranges : Type: (array)
variable "hx_replication_ip_start_addr" {
  type        = string
  description = "The start IPv4 address of the range."
}
variable "hx_replication_ip_end_addr" {
  type        = string
  description = "The end IPv4 address of the range."
}
variable "hx_replication_netmask" {
  type        = string
  description = "The netmask specified in dot decimal notation."
}
variable "hx_replication_gateway" {
  type        = string
  description = "The default gateway for the start and end IPv4 addresses."
}


# Ext iSCSI Policy 
variable "hx_ext_iscsi_admin_state" {
  type        = bool
  description = "Enable or disable external FCoE storage configuration"
}
variable "hx_iscsi_exta_name" {
  type        = string
  description = "Path_A vlan name"
}
variable "hx_iscsi_exta_vlan_id" {
  type        = number
  description = "Path_A vlan id"
}
variable "hx_iscsi_extb_name" {
  type        = string
  description = "Path_B vlan name"
}
variable "hx_iscsi_extb_vlan_id" {
  type        = number
  description = "Path_B vlan id"
}


# Ext FC storage policy
variable "hx_fc_admin_state" {
  type        = bool
  description = "Enables or disables external FC storage configuration"
}
variable "hx_fc_exta_vsan_name" {
  type        = string
  description = "path_a vsan name"
}
variable "hx_fc_exta_vsan_id" {
  type        = number
  description = "path_a vsan id"
}
variable "hx_fc_extb_vsan_name" {
  type        = string
  description = "path_b vsan name"
}
variable "hx_fc_extb_vsan_id" {
  type        = number
  description = "path_b vsan id"
}
variable "hx_fc_wwxn_prefix_start_addr" {
  type        = string
  description = "The start WWxN prefix of a WWPN/WWNN range in the form of 20:00:00:25:B5:XX"
}
variable "hx_fc_wwxn_prefix_end_addr" {
  type        = string
  description = "The end WWxN prefix of a WWPN/WWNN range in the form of 20:00:00:25:B5:XX"
}

# cluster_profile
variable "hx_data_ip_address" {
  type        = string
  description = "hx data cluster ip"
}
variable "hx_hypervisor_type" {
  type        = string
  description = "hx hypervisor type"
}
variable "hx_mac_address_prefix" {
  type        = string
  description = "hx mac address prefix"
}
variable "hx_host_name_prefix" {
  type        = string
  description = "The specified Hostname Prefix will be applied to all nodes"
}
variable "hx_mgmt_ip_address" {
  type        = string
  description = "hx mgmt cluster ip"
}
variable "hx_mgmt_platform" {
  type        = string
  description = "Depoloyment type: FI or EDGE "
}
variable "hx_replication" {
  type        = number
  description = "hx replication count"
}
variable "hx_storage_data_vlan_name" {
  type        = string
  description = "hx storage data vlan name"
}
variable "hx_storage_data_vlan_id" {
  type        = number
  description = "hx storage data vlan id"
}

# node_config_policy
# variable "hx_servers" {
#   type        = map(string)
#   description = "HX server list for the cluster"
# }

variable "names" {
  type    = list(string)
  default = ["dev-prof", "lab-prof", "stage-prof"]
}

variable "server_names" {
  type = list
}
