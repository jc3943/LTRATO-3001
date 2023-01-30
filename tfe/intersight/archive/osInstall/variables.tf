# Intersight Access API Key
variable "api_key" {
  type        = string
  description = "Intersight API key"
}

variable "secret_key" {
  type        = string
  description = "Intersight Secret Key file"
  default     = "SecretKey.txt"
}

variable "endpoint" {
  type        = string
  description = "Intersight URL"
  default     = "https://intersight.com"
}

variable "org_name" {
  type        = string
  description = "Organization Name for the desired object"
}

# Common
# Tags
variable "tags" {
  type = map(string)
  default = {
    key1   = "DC"
    value1 = "SJ"
    key2   = "ENV"
    value2 = "LAB"
  }
}

# create_os_repo  
variable "repo_name" {
  type        = string
  description = "The name of the file. It is populated as part of the image import operation."
  default     = "esxi_6.7.0_cisco_custom_iso"
}
variable "repo_nr_version" {
  type        = string
  description = "Vendor OS Version" # Options: check Intersight GUI
  default     = "ESXi 6.7 U3"
}
variable "repo_vendor" {
  type        = string
  description = "Vendor Name" # Options: check Intersight GUI
  default     = "VMware"
}
variable "repo_description" {
  type        = string
  description = "Repo Description" # # Options: check Intersight GUI
  default     = "ESXi 6.7 U3 Cisco Custom ISO"
}
variable "repo_source_os_iso_path" {
  type        = string
  description = "#HTTP/HTTPS link to the image. Accepted formats are HTTP[s]://server-hostname/share/image or HTTP[s]://serverip/share/image. "
}

# Common attributes between OS/SCU Resources: 
variable "repo_source_object_type" {
  type        = string
  description = "Repo Type"
  default     = "softwarerepository.HttpServer" # softwarerepository.HttpServer, softwarerepository.CifsServer, softwarerepository.NfsServer
}

variable "repo_source_cifs_mount_options" {
  type        = string
  description = "For CIFS, leave the field blank or enter one or more comma seperated options from the following. For Example, \" \" , \" soft \" , \" soft , nounix \" . * soft. * nounix. * noserviceino. * guest. * USERNAME=VALUE. * PASSWORD=VALUE. * sec=VALUE (VALUE could be None, Ntlm, Ntlmi, Ntlmssp, Ntlmsspi, Ntlmv2, Ntlmv2i)."
}

variable "repo_source_nfs_mount_options" {
  type        = string
  description = "For NFS, leave the field blank or enter one or more comma seperated options from the following.For Example, \" \" , \" ro \" , \" ro , rw \" . * ro. * rw. * nolock. * noexec. * soft. * PORT=VALUE. * timeo=VALUE. * retry=VALUE."
}
variable "repo_source_user" {
  type        = string
  description = "Username as configured on the HTTP[S] server for user authentication. It is generally required to authenticate user provided HTTP[S] based software repositories."
}

variable "repo_source_password" {
  type        = string
  description = "Password as configured on the HTTP[S] server for user authentication. It is generally required to authenticate user provided HTTP[S] based software repositories."
}


# create_scu_repo 
variable "repo_source_scu_iso_path" {
  type        = string
  description = "#HTTP/HTTPS link to the image. Accepted formats are HTTP[s]://server-hostname/share/image or HTTP[s]://serverip/share/image. "
}
variable "scu_name" {
  type = string
}
variable "scu_description" {
  type = string
}
variable "scu_nr_version" {
  type        = string
  description = "SCU Version"
}
variable "scu_supported_models" {
  type        = list(string)
  description = "SCU Supported UCS Servers"
  default = [
    "C-series",
  ]
}

# os_install
variable "os_install_server_selector" {
  type        = string
  description = "Server serial where we are installing OS"
}
variable "os_install_configuration_file_selector" {
  type        = string
  description = "Cisco provided OS configuration file name"
}

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
variable "os_tmpl_name" {
  type        = string
  description = "Template name"
}
variable "os_tmpl_file" {
  type        = string
  description = "Template file name"
}

