# 1. Automatyczne utworzenie sekretu w klastrze AKS (zastepuje reczne kubectl create secret)
resource "kubernetes_secret" "learningsteps_secrets" {
  metadata {
    name      = "learningsteps-secrets"
    namespace = "default"
  }

  data = {
    POSTGRES_PASSWORD = random_password.db_password.result
    DATABASE_URL      = "postgresql://pgadmin:${random_password.db_password.result}@postgres-svc:5432/learningsteps"
  }

  depends_on = [azurerm_kubernetes_cluster.aks]
}

# 2. Automatyczna aktualizacja GitHub Actions Secrets (zastepuje reczne gh secret set)
resource "github_actions_secret" "acr_name" {
  repository      = "learningsteps"
  secret_name     = "ACR_NAME"
  plaintext_value = azurerm_container_registry.acr.name
}

resource "github_actions_secret" "acr_login_server" {
  repository      = "learningsteps"
  secret_name     = "ACR_LOGIN_SERVER"
  plaintext_value = azurerm_container_registry.acr.login_server
}

resource "github_actions_secret" "aks_cluster_name" {
  repository      = "learningsteps"
  secret_name     = "AKS_CLUSTER_NAME"
  plaintext_value = azurerm_kubernetes_cluster.aks.name
}

resource "github_actions_secret" "azure_rg" {
  repository      = "learningsteps"
  secret_name     = "AZURE_RG"
  plaintext_value = azurerm_resource_group.rg.name
}
