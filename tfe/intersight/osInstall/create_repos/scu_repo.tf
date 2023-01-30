locals {
  scu_sources = {
    https = "softwarerepository.HttpServer",
    cifs = "softwarerepository.CifsServer",
    nfs = "softwarerepository.NfsServer"
  }
  scu_source_type = lookup(local.scu_sources, var.object_type, "https" )
}

resource "intersight_firmware_server_configuration_utility_distributable" "scu_repo" {
  name             = var.scu_name
  nr_version       = var.scu_nr_version
  supported_models = var.scu_supported_models
  description      = var.scu_description
  # Uncomment when Organization option is added to Intersight Provider
  # Issue: https://github.com/CiscoDevNet/terraform-provider-intersight/issues/231
  #organization {
  #  object_type = "organization.Organization"
  #  moid = data.intersight_organization_organization.org.results[0].moid
  #}
  dynamic "tags" {
    for_each = var.Tags
    content {
      key   = tags.value.Key
      value = tags.value.Value
    }
  }
#  catalog {
#    selector    = "Name eq 'user-catalog' and Organization/Moid eq '${data.intersight_organization_organization.org.results[0].moid}'"
#    object_type = "softwarerepository.Catalog"
#  }
  nr_source {
    object_type = local.scu_source_type # var.repo_source_object_type
    additional_properties = jsonencode({
      # HTTPS
      LocationLink = var.repo_source_scu_iso_path
      Username     = var.repo_source_user
      Password     = var.repo_source_password

      # CIFS
      # FileLocation = var.repo_source_scu_iso_path
      # MountOption  = var.repo_source_cifs_mount_options
      # Username     = var.repo_source_user
      # Password     = var.repo_source_password

      # NFS
      # FileLocation = var.repo_source_scu_iso_path
      # MountOptions = var.repo_source_nfs_mount_options
    })
  }
}
