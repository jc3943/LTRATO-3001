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
      # private key path
      private_key = "../creds/ansible.key"
      # Certificate Name
      cert_name = "ansible"
      # cisco-aci url
      url      = "https://172.0.1.101"
      insecure = true
}

resource "aci_tenant" "example" {
  name        = "demo_tenant"
  description = "from terraform"
  annotation  = "tag"
  name_alias  = "tenant"
}