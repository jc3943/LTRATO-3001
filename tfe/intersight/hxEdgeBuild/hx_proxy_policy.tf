/*resource "intersight_hyperflex_proxy_setting_policy" "hx_proxy_setting_policy" {
  name        = "${var.cluster_name}_proxy_settings"
  description = "HX Proxy Settings"
  hostname    = var.hx_proxy_ip
  password    = var.hx_proxy_password
  port        = var.hx_proxy_port
  username    = var.hx_proxy_username
  organization {
    object_type = "organization.Organization"
    moid        = data.intersight_organization_organization.org_data.results[0].moid
  }
  tags {
    key   = var.tag_key1
    value = var.tag_value1
  }
}*/
