terraform {
  required_providers {
    aci = {
      source = "CiscoDevNet/aci"
      version = "2.4.0"
    }
  }
}

provider "aci" {
      # cisco-aci user name
      username = "ansible"
      #password = "DEVP@ssw0rd"
      # private key path
      private_key = "../creds/ansible.key"
      # Certificate Name
      cert_name = "ansible"
      # cisco-aci url
      url      = "https://172.0.1.101"
      insecure = true
}

locals {
  instances = csvdecode(file("./tenant.csv"))
  #instances = csvdecode(local.csv_data)
}

resource "aci_tenant" "aci-tenant" {
  for_each = { for inst in local.instances : inst.bridgeDomain => inst }
  name        = each.value.tenant
  description = "from terraform"
  annotation  = "tag"
  name_alias  = "tenant"
}

resource "aci_vrf" "aci-vrf" {
  for_each = { for inst in local.instances : inst.bridgeDomain => inst }
  name        = each.value.vrf
  description = "from terraform"
  annotation  = "tag"
  name_alias  = "vrf"
}