resource "intersight_hyperflex_cluster_profile" "hx_cluster_profile" {
  depends_on = [intersight_hyperflex_auto_support_policy.hx_auto_support_policy,
    intersight_hyperflex_cluster_network_policy.hx_network_config_policy,
    intersight_hyperflex_cluster_storage_policy.hx_storage_config_policy,
    intersight_hyperflex_local_credential_policy.hx_local_credential_policy,
    intersight_hyperflex_node_config_policy.hx_node_config_policy,
    intersight_hyperflex_software_version_policy.hx_software_version_policy,
    intersight_hyperflex_sys_config_policy.hx_sys_config_policy,
    intersight_hyperflex_vcenter_config_policy.hx_vcenter_policy
  ]
  name        = var.cluster_name
  description = "${var.cluster_name} HX Cluster Profile"
  organization {
    object_type = "organization.Organization"
    moid        = data.intersight_organization_organization.org_data.results[0].moid
  }
  tags {
    key   = var.tag_key1
    value = var.tag_value1
  }
  data_ip_address    = var.hx_data_ip_address
  hypervisor_type    = var.hx_hypervisor_type
  mac_address_prefix = var.hx_mac_address_prefix
  mgmt_ip_address    = var.hx_mgmt_ip_address
  mgmt_platform      = var.hx_mgmt_platform
  replication        = var.hx_replication
  host_name_prefix   = var.hx_host_name_prefix
  storage_data_vlan {
    name    = var.hx_storage_data_vlan_name
    vlan_id = var.hx_storage_data_vlan_id
  }
  local_credential {
    moid = intersight_hyperflex_local_credential_policy.hx_local_credential_policy.moid
  }
  sys_config {
    moid = intersight_hyperflex_sys_config_policy.hx_sys_config_policy.moid
  }
  vcenter_config {
    moid = intersight_hyperflex_vcenter_config_policy.hx_vcenter_policy.moid
  }
  cluster_storage {
    moid = intersight_hyperflex_cluster_storage_policy.hx_storage_config_policy.moid
  }
  auto_support {
    moid = intersight_hyperflex_auto_support_policy.hx_auto_support_policy.moid
  }
  node_config {
    moid = intersight_hyperflex_node_config_policy.hx_node_config_policy.moid
  }
  cluster_network {
    moid = intersight_hyperflex_cluster_network_policy.hx_network_config_policy.moid
  }
  /*proxy_setting {
    moid = intersight_hyperflex_proxy_setting_policy.hx_proxy_setting_policy.moid
  }*/
  /*
  ext_fc_storage {
    moid = intersight_hyperflex_ext_fc_storage_policy.hx_ext_fc_storage_policy.moid
  }
  ext_iscsi_storage {
    moid = intersight_hyperflex_ext_iscsi_storage_policy.hx_ext_iscsi_policy.moid
  }
  */
  software_version {
    moid = intersight_hyperflex_software_version_policy.hx_software_version_policy.moid
  }
  # action = var.hx_profile_action
}
