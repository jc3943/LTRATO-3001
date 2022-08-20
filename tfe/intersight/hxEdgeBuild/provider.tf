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
  secretkey = var.secret_key
  endpoint = var.endpoint
}
