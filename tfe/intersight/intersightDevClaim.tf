#Authored: Jeff Comer

locals {
  instances = csvdecode(file("./hostIpAddrs.csv"))
}

resource "intersight_appliance_device_claim" "intersight_imc_claim" {
  for_each = { for inst in local.instances : inst.cimc => inst }
  hostname        = each.value.cimc
  platform_type = "IMC"
  username  = var.cimc_user
  password = var.cimc_pw
}
