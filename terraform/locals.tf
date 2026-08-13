locals {
  project_name = "network-automation"
  environment  = "lab"

  common_tags = {
    Project     = local.project_name
    Environment = local.environment
    ManagedBy   = "Terraform"
  }
}