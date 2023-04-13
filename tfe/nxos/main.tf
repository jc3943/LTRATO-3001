terraform {
  required_version = ">= 1.1.0"

  required_providers {
    nxos = {
      source  = "netascode/nxos"
      version = ">=0.3.19"
    }
    utils = {
      source  = "netascode/utils"
      version = ">= 0.1.1"
    }
  }
}
provider "nxos" {
  username = admin
  password = cisco!123
  devices  = local.devices
}
locals {
  model = yamldecode(data.utils_yaml_merge.model.output)

  devices = concat(lookup(local.model.fabric.inventory, "leafs", []), lookup(local.model.fabric.inventory, "spines", []))
  leafs   = toset([for leaf in lookup(local.model.fabric.inventory, "leafs", []) : leaf.name])
  spines  = toset([for spine in lookup(local.model.fabric.inventory, "spines", []) : spine.name])
}

data "utils_yaml_merge" "model" {
  input = [for file in fileset(path.module, "../../vars/nxos-cpoc-mod0/nxos/*.yaml") : file(file)]
}

module "nxos_features" {
  source  = "netascode/features/nxos"
  version = ">= 0.0.1"
  device  = local.devices

  bfd     = true
  ospf    = true
  bgp     = true
  pim     = true
  udld    = true
  interface_vlane = true
  hsrp    = true
  lacp    = true
  dhcp    = true
  vpc     = true
  lldp    = true

}

