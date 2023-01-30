# Common
variable "org_name" {
  type = string
}

variable "server_serial" {
  type = string
}

variable "os_config_file" {
  type = string
}

variable "os_repo_name" {
  type = string
}

variable "scu_repo_name" {
  type = string
}
# os_install
# variable "os_install_server_selector" {
#   type        = string
#   description = "Server serial where we are installing OS"
# }
# variable "os_install_configuration_file_selector" {
#   type        = string
#   description = "Cisco provided OS configuration file name"
# }

variable "os_hostname" {
  type        = string
  description = "OS Hostname"
}
variable "os_ip_config_type" {
  type        = string
  description = "OS Configuration Type"
}

## OS IP Info
variable "os_ipv4_addr" {
  type        = string
  description = "OS IPv4 address"
}
variable "os_ipv4_netmask" {
  type        = string
  description = "OS IPv4 Subnet mask"
}
variable "os_ipv4_gateway" {
  type        = string
  description = "OS IPv4 Gateway"
}
variable "os_ipv4_dns_ip" {
  type        = string
  description = "IPv4 DNS server IP"
}
variable "os_root_password" {
  type        = string
  description = "OS Password"
}
variable "os_answers_nr_source" {
  type        = string
  description = "Source of Answer file"
  default     = "Template" # Template for cisco provided source files
}
variable "os_answers_netDev" {
  type        = string
  description = "management network vmnic"
}
variable "os_answers_vlanId" {
  type        = number
  description = "management network vlan"
}