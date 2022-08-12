terraform {
  required_providers {
    intersight = {
      source = "CiscoDevNet/intersight"
      //version = "1.0.31"
    }
  }
}

provider "intersight" {
  apikey    = "6273ddc07564612d30091b97/6273e4cc7564612d300964b9/62f53d6e7564612d30253ff4"
  secretkey = "../../creds/qa-isight-SecretKey.txt"
  endpoint = "https://qa-intersight.thor.iws.navy.mil"
}

locals {
  instances = csvdecode(file("./hostIpAddrs.csv"))
}

resource "intersight_appliance_device_claim" "intersight_imc_claim" {
  for_each = { for inst in local.instances : inst.cimc => inst }
  hostname        = each.value.cimc
  platform_type = "IMC"
  username  = "admin"
  password = "DEVP@ssw0rd"
}
