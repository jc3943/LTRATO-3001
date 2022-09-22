resource "intersight_hyperflex_vcenter_config_policy" "hx_vcenter_policy" {
  name        = "${var.cluster_name}_vcenter_config"
  description = "HX vCenter Config Policy"
  organization {
    object_type = "organization.Organization"
    moid        = data.intersight_organization_organization.org_data.results[0].moid
  }
  tags {
    key   = var.tag_key1
    value = var.tag_value1
  }
  data_center = var.hx_vcenter_dc_name
  hostname    = var.hx_vcenter_ip
  password    = base64decode(var.hx_vcenter_password)
  username    = var.hx_vcenter_username
}
