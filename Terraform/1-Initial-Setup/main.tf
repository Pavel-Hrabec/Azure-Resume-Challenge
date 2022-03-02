# This will be used to deploy infrastructure for Azure Cloud Resume Challenge

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
    }
  }
}

provider "azurerm" {
  features {}
}

#create resource group
resource "azurerm_resource_group" "rg" {
    name     = var.resourceGroupName
    location = var.location
}
