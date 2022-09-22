resource "intersight_hyperflex_local_credential_policy" "hx_local_credential_policy" {
  name        = "${var.cluster_name}_security_config"
  description = "HX Local Credentials Policy"
  organization {
    object_type = "organization.Organization"
    moid        = data.intersight_organization_organization.org_data.results[0].moid
  }
  tags {
    key   = var.tag_key1
    value = var.tag_value1
  }
  factory_hypervisor_password = var.hx_factory_hypervisor_password
  hypervisor_admin            = var.hx_hypervisor_admin_user
  hypervisor_admin_pwd        = base64decode(var.hx_hypervisor_admin_pwd)
  hxdp_root_pwd               = base64decode(var.hx_hxdp_root_pwd)
}
