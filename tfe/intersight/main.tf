#Authored: Jeff Comer
terraform {
  required_providers {
    intersight = {
      source = "CiscoDevNet/intersight"
      version = "1.0.31"
    }
  }
}

provider "intersight" {
  apikey = var.api_key
  secretkeyfile = var.api_key_file
  endpoint = var.api_endpoint
}