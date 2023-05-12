#!/usr/bin/env bash

terraform init
terraform destroy
rm -rf .terraform
rm -rf terraform.tfstate*
rm -rf .terraform.tfstate*
sed 's/Bonjour/Hello/' -i default.html.tpl
