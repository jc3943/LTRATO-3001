locals {
  os_sources = {
    https = "softwarerepository.HttpServer",
    cifs = "softwarerepository.CifsServer",
    nfs = "softwarerepository.NfsServer"
  }
  os_source_type = lookup(local.os_sources, var.object_type, "https" )
}

resource "intersight_softwarerepository_operating_system_file" "os_repo" {
  name        = var.repo_name
  nr_version  = var.repo_nr_version
  vendor      = var.repo_vendor
  description = var.repo_description
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
    object_type = local.os_source_type # var.repo_source_object_type
    additional_properties = jsonencode({
      # HTTPS
      LocationLink = var.repo_source_os_iso_path
      Username     = var.repo_source_user
      Password     = var.repo_source_password

      # CIFS
      # FileLocation = var.repo_source_os_iso_path
      # MountOption  = var.repo_source_cifs_mount_options
      # Username     = var.repo_source_user
      # Password     = var.repo_source_password

      # NFS
      # FileLocation = var.repo_source_os_iso_path
      # MountOptions = var.repo_source_nfs_mount_options
    })
  }
}

