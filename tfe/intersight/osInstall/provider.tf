terraform {
  #required_version = ">= 0.13.5"
  required_providers {
    intersight = {
      source = "CiscoDevNet/intersight"
      version = "1.0.32"
    }
  }
}

provider "intersight" {
  apikey    = var.api_key
  secretkey = var.secret_key
  endpoint  = var.endpoint
}
