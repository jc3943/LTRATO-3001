resource "intersight_os_install" "os_install" {
  name = "InstallTemplate"
  description    = "Install ESXi 6.7"
  organization {
    object_type = "organization.Organization"
    moid = data.intersight_organization_organization.org.results[0].moid
  }
  server {
    object_type = data.intersight_compute_physical_summary.server.results[0].source_object_type
    moid        = data.intersight_compute_physical_summary.server.results[0].moid
  }
  image {
    object_type = "softwarerepository.OperatingSystemFile"
    moid        = data.intersight_softwarerepository_operating_system_file.os_repo.results[0].moid
    #selector    = "$filter=results[0].Version eq 'ESXi 6.7 U3'"
  }
  osdu_image {
    object_type = "firmware.ServerConfigurationUtilityDistributable"
    moid        = data.intersight_firmware_server_configuration_utility_distributable.scu_repo.results[0].moid
    #selector    = "$filter=results[0].Version eq '6.1.3c'"
  }
  configuration_file {
    object_type = "os.ConfigurationFile"
    moid        = data.intersight_os_configuration_file.os_config.results[0].moid
    #selector    = "$filter=Name eq 'esxi-cfg-kst'"
  }
  answers {
    hostname       = var.os_hostname
    ip_config_type = var.os_ip_config_type
    # IpV4Config = {
    ip_configuration {
      additional_properties = jsonencode({
        IpV4Config = {
          IpAddress = var.os_ipv4_addr
          Netmask   = var.os_ipv4_netmask
          Gateway   = var.os_ipv4_gateway
        }
      })
      object_type = "os.Ipv4Configuration"
    }
    is_root_password_crypted = false
    nameserver               = var.os_ipv4_dns_ip
    root_password            = var.os_root_password
    nr_source                = var.os_answers_nr_source
    network_device           = var.os_answers_netDev
  }
  install_method = "vMedia"
  install_target {
    object_type = "os.VirtualDrive"
    additional_properties = jsonencode({
      ObjectType              = "os.VirtualDrive"
      Id                      = "0"
      Name                    = "RAID0_1"
      StorageControllerSlotId = "MRAID"
    })
  }
  operating_system_parameters {
    object_type = "os.VmwareParameters"
    additional_properties = jsonencode({
      ObjectType              = "os.VmwareParameters"
      Vlanid                  = var.os_answers_vlanId
    })
  }
}
