terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}
 
resource "aws_ecr_repository" "lab" {
  name = var.repository_name



  tags = local.common_tags
}

data "aws_ecr_repository" "deployment" {
  name = "network-automation-interview-lab"
}