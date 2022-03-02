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

# Create resource group - run into error that resource already exists
# Will import this instead
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.resource_group_location
}

/*
# Create cosmos db account 
resource "azurerm_cosmosdb_account" "acc" {
  name = var.cosmos_db_account_name
  location = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  offer_type = "Standard"
  kind = "GlobalDocumentDB"
  
  consistency_policy {
    consistency_level = "Session"
  }
  
  geo_location {
    location = var.failover_location
    failover_priority = 1
  }
  
  geo_location {
    location = var.resource_group_location
    failover_priority = 0
  }
}
*/

