terraform {
  #required_version = ">= 1.3.6"
  required_providers {
    intersight = {
      source = "CiscoDevNet/intersight"
      version = "1.0.35"
    }
  }
}

provider "intersight" {
  apikey    = "6273ddc07564612d30091b97/6273e4cc7564612d300964b9/62f53d6e7564612d30253ff4"
  secretkey = "../../../../creds/qa-isight-SecretKey.txt"
  endpoint  = "https://qa-intersight.thor.iws.navy.mil"
}
