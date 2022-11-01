resource "intersight_os_bulk_install_info" "os_install" {
  name = "../../../vmware/sandbox-esxi-bm2.csv"
  file_content = file("../../../vmware/sandbox-esxi-bm2.csv")
/*  server {
    object_type = "compute.RackUnit"
    selector    = var.os_install_server_selector
  }
  image {
    object_type = "softwarerepository.OperatingSystemFile"
    moid        = intersight_softwarerepository_operating_system_file.esxi_custom_iso.moid
  }
  osdu_image {
    moid        = intersight_firmware_server_configuration_utility_distributable.scu_ucsc.moid
    object_type = "firmware.ServerConfigurationUtilityDistributable"
  } */
/*  configuration_file {
    object_type = "os.ConfigurationFile"
    selector    = var.os_install_configuration_file_selector
  } */

/*  answers {
    hostname       = var.os_hostname
    ip_config_type = var.os_ip_config_type
    ip_configuration = [{
      class_id      = "os.PlaceHolder"
      additional_properties = jsonencode({
        IpV4Config = {
          IpAddress = "172.16.115.41"
          NetMask   = "255.255.252.0"
          GateWay   = "172.16.115.254"
          dns1      = "172.16.20.101"
          dns2      = "172.20.1.254"
          syslog    = "172.16.10.99"
          vlanId    = "1200"
          NetworkDevice1 = "vmnic5"
        }
      })
      object_type = "os.Ipv4Configuration"
    }]
    is_root_password_crypted = false
    nameserver               = var.os_ipv4_dns_ip
    root_password            = var.os_root_password
    nr_source                = var.os_answers_nr_source
  } */
/*  answers {
    #answer_file = file("../../../vmware/answers.json")
    nr_source   = "None"
    object_type = "os.Answers"
  } */
  #description    = "Install ESXi 6.7 U3"
  #install_method = "vMedia"
  organization {
    object_type = "organization.Organization"
    moid        = "6273e3fd6972652d3030ae8d"
  }
/*  install_target {
    additional_properties = jsonencode({
      Id                      = "0"
      Name                    = "RAID0_1"
      StorageControllerSlotId = "MRAID"
    })
    object_type = "os.VirtualDrive"
  } */
}
