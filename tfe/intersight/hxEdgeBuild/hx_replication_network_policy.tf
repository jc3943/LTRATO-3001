resource "intersight_hyperflex_cluster_replication_network_policy" "hx_replication_network_policy" {
  name        = "${var.cluster_name}_replication_network"
  description = "HX Replication Network Policy"
  organization {
    object_type = "organization.Organization"
    moid        = data.intersight_organization_organization.org_data.results[0].moid
  }
  tags {
    key   = var.tag_key1
    value = var.tag_value1
  }
  replication_vlan {
    name    = var.hx_replication_vlan_name
    vlan_id = var.hx_replication_vlad_id
  }
  replication_bandwidth_mbps = var.hx_replication_bandwidth_mbps
  replication_mtu            = var.hx_replication_mtu
  replication_ipranges {
    start_addr = var.hx_replication_ip_start_addr
    end_addr   = var.hx_replication_ip_end_addr
    netmask    = var.hx_replication_netmask
    gateway    = var.hx_replication_gateway
  }
}
