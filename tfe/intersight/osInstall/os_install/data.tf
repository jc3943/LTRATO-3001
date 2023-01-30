data "intersight_organization_organization" "org" {
  name = var.org_name
}

data "intersight_compute_physical_summary" "server" {
    serial = var.server_serial
}

data "intersight_os_configuration_file" "os_config" {
    name = var.os_config_file
}

data "intersight_softwarerepository_operating_system_file" "os_repo" {
    name = var.os_repo_name
}

data "intersight_firmware_server_configuration_utility_distributable" "scu_repo" {
    name = var.scu_repo_name
}
