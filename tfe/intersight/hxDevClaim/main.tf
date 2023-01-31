#Authored: Jeff Comer
terraform {
  required_providers {
    intersight = {
      source = "CiscoDevNet/intersight"
      version = "1.0.35"
    }
  }
}

provider "intersight" {
  apikey = var.api_key
  secretkey = var.api_key_file
  endpoint = var.api_endpoint
}