resource "intersight_softwarerepository_operating_system_file" "esxi_custom_iso" {
  name        = var.repo_name        # "esxi_6.7.0_cisco_custom_iso"
  nr_version  = var.repo_nr_version  # "ESXi 6.7 U3"
  vendor      = var.repo_vendor      # "VMware"
  description = var.repo_description # "ESXi 6.7 U3 Cisco Custom ISO"
  tags {
    key   = var.tags.key1
    value = var.tags.value1
  }
  tags {
    key   = var.tags.key2
    value = var.tags.value2
  }
  nr_source {
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
    object_type = var.repo_source_object_type
  }
}
