resource "intersight_firmware_server_configuration_utility_distributable" "scu_ucsc" {
  name             = var.scu_name
  nr_version       = var.scu_nr_version
  supported_models = var.scu_supported_models
  description      = var.scu_description
  tags {
    key   = var.tags.key1
    value = var.tags.value1
  }
  tags {
    key   = var.tags.key2
    value = var.tags.value2
  }
  nr_source {
    object_type = var.repo_source_object_type
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
