terraform {
  required_version = ">= 1.5.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.90"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
    # [DODANE]: Provider do tworzenia sekretow bezposrednio w klastrze AKS
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.30"
    }
    # [DODANE]: Provider do automatycznej aktualizacji GitHub Actions Secrets
    github = {
      source  = "integrations/github"
      version = "~> 6.2"
    }
  }
}

provider "azurerm" {
  features {}
}

# [DODANE]: Konfiguracja dostepu Terraforma do nowo utworzonego AKS
provider "kubernetes" {
  host                   = azurerm_kubernetes_cluster.aks.kube_config[0].host
  client_certificate     = base64decode(azurerm_kubernetes_cluster.aks.kube_config[0].client_certificate)
  client_key             = base64decode(azurerm_kubernetes_cluster.aks.kube_config[0].client_key)
  cluster_ca_certificate = base64decode(azurerm_kubernetes_cluster.aks.kube_config[0].cluster_ca_certificate)
}

# [DODANE]: Konfiguracja dostepu do GitHuba (pobiera token ze zmiennej GITHUB_TOKEN)
provider "github" {
  owner = "CyberNoon"
}
