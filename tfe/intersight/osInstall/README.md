[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/sandkum5/terraform_intersight_os_install)
# Install OS on UCS servers using terraform Intersight provider

* This module installs an OS on a UCS Server using terraform intersight provider

## Dirs
- create_repos 
  - To create an Operating System(OS) and Server Configuration Utility(SCU) repos
 
- os_install
  - To Trigger Operating System(OS) Install Workflow
  
## Below is a list of policies created as part of the process: 
- Operating Systems Image repo
- Server Configuration Utilities repo
- Install Operating system 

## Requirements
* Terraform v1.3.6
* Intersight Provider version 1.0.34
* git 

## Usage
* Create an account in intersight.com. 
* Login to Intersight, go to settings and generate API key. Download the SecretKey.txt file and copy the API key. 
* Download and install Terraform
<https://www.terraform.io/downloads.html>
* Clone the repository
```txt
git clone https://github.com/sandkum5/terraform_intersight_os_install.git

To create OS and SCU Repos:
cd terraform_intersight_os_install/create_repos

To Trigger OS installation Workflow:
cd terraform_intersight_os_install/os_install
```

* Copy the SecretKey.txt file in the os_install directory. 
* Add the API Key to the ApiKey.txt file and the rest of the environment variables in the `<env>`.tfvars template files. Filename can be re-named as `<new-filename>`.tfvars.

* Initialize Terraform. 
  Note: This step automatically downloads intersight provider plugin. 

```txt
terraform init
```

* Create Terraform exacution plan

```txt
terraform plan
```

* Apply the configuration

```txt
terraform apply
```

When asked to enter a value, enter **"yes"**.

* Destroy the Terraform managed infrastructure

```txt
terraform destroy
```

To get more details on Intersight, terraform provider for intersight, how to create an intersight account, how to Generate API keys, refer: 
https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/2201041-intersight-terrafirma-wp.html 


## Terraform Workspaces 
* Use terraform workspaces to reuse the same config file for different environments. 

* Create a new workspace : 
```txt
  terraform workspace new WORKSPACE_NAME      # creates and moves to the new workspace 
```
* To list workspaces     
```txt
  terraform workspace list          # "*" indicates the current selected workspace
```
* To switch workspace    
```txt
terraform workspace select WORKSPACE_NAME     # Move to a different namespace
```

* Create a separate <env_name>.tfvars file for each environment 
* Use below commands in the respective workspace to create the policies. 
```txt
terraform plan -var-file=<env_name>.tfvars   
terraform apply -var-file=<env_name>.tfvars
```
* Use the provided sample env.tfvars template for all the environment variables configuration. 



### Additional intersight modules: 
https://github.com/CiscoDevNet/intersight-terraform-modules

https://github.com/sandkum5/terraform-intersight-hx-edge-deploy

https://github.com/sandkum5/intersight-terraform-C-Series

