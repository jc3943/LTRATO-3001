# Common
variable "Tags" {
  type = list(object({ Key = string, Value = string }))
}

variable "object_type" {
  type = string
  description = "Values: https, cifs, nfs"
}

variable "enable_https" {
  type = bool
}

variable "enable_cifs" {
  type = bool
}

variable "enable_nfs" {
  type = bool
}

# create_os_repo
variable "repo_name" {
  type        = string
  description = "The name of the file. It is populated as part of the image import operation."
}
variable "repo_nr_version" {
  type        = string
  description = "Vendor OS Version" # Options: check Intersight GUI
}
variable "repo_vendor" {
  type        = string
  description = "Vendor Name" # Options: check Intersight GUI
}
variable "repo_description" {
  type        = string
  description = "Repo Description" # # Options: check Intersight GUI
}
variable "repo_source_os_iso_path" {
  type        = string
  description = "#HTTP/HTTPS link to the image. Accepted formats are HTTP[s]://server-hostname/share/image or HTTP[s]://serverip/share/image. "
}

# Common attributes between OS/SCU Resources:
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
}
