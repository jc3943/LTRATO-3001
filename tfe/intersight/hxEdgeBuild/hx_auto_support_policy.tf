resource "intersight_hyperflex_auto_support_policy" "hx_auto_support_policy" {
  name        = "${var.cluster_name}-auto-support"
  description = "Auto Support Policy"
  organization {
    object_type = "organization.Organization"
    moid        = data.intersight_organization_organization.org_data.results[0].moid
  }
  tags {
    key   = var.tag_key1
    value = var.tag_value1
  }
  service_ticket_receipient = var.hx_auto_support_service_ticket_receipient
  admin_state               = var.hx_auto_support_admin_state
}
