resource "intersight_hyperflex_ext_iscsi_storage_policy" "hx_ext_iscsi_policy" {
  name        = "${var.cluster_name}_ext_iscsi_storage"
  description = "HX Ext iSCSI Storage Policy"
  organization {
    object_type = "organization.Organization"
    moid        = data.intersight_organization_organization.org_data.results[0].moid
  }
  tags {
    key   = var.tag_key1
    value = var.tag_value1
  }
  admin_state = var.hx_ext_iscsi_admin_state
  exta_traffic {
    name    = var.hx_iscsi_exta_name
    vlan_id = var.hx_iscsi_exta_vlan_id
  }
  extb_traffic {
    name    = var.hx_iscsi_extb_name
    vlan_id = var.hx_iscsi_extb_vlan_id
  }
}
