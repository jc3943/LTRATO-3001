resource "intersight_hyperflex_ext_fc_storage_policy" "hx_ext_fc_storage_policy" {
  name        = "${var.cluster_name}_ext_fc_storage"
  description = "External FC Storage Policy"
  organization {
    object_type = "organization.Organization"
    moid        = data.intersight_organization_organization.org_data.results[0].moid
  }
  tags {
    key   = var.tag_key1
    value = var.tag_value1
  }
  admin_state = var.hx_fc_admin_state
  exta_traffic {
    name    = var.hx_fc_exta_vsan_name
    vsan_id = var.hx_fc_exta_vsan_id
  }
  extb_traffic {
    name    = var.hx_fc_extb_vsan_name
    vsan_id = var.hx_fc_extb_vsan_id
  }
  wwxn_prefix_range {
    start_addr = var.hx_fc_wwxn_prefix_start_addr
    end_addr   = var.hx_fc_wwxn_prefix_end_addr
  }
}
