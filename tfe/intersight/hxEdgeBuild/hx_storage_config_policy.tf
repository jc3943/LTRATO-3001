resource "intersight_hyperflex_cluster_storage_policy" "hx_storage_config_policy" {
  name        = "${var.cluster_name}_storage_config"
  description = "HX Storage Configuration"
  organization {
    object_type = "organization.Organization"
    moid        = data.intersight_organization_organization.org_data.results[0].moid
  }
  tags {
    key   = var.tag_key1
    value = var.tag_value1
  }
  disk_partition_cleanup = var.hx_disk_partition_cleanup
  vdi_optimization       = var.hx_vdi_optimization
  # logical_avalability_zone_config = [{
  #   auto_config = var.hx_logical_avalability_zone_config
  #   "additional_properties" = ""
  #   "class_id" = ""
  #   "object_type" = ""
  # }]
}
