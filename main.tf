terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "drill_rg" {
  name     = "rg-drill-training"
  location = "West Europe"
}

resource "azurerm_storage_account" "drill_st" {
  # RANDOMIZE THIS NAME (must be globally unique)
  name                     = "stdrillcalin009" 
  resource_group_name      = azurerm_resource_group.drill_rg.name
  location                 = azurerm_resource_group.drill_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = {
    Environment = "Drill"
  }
}