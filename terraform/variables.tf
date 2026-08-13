variable "aws_region" {
  type        = string
  description = "AWS region to deploy resources into"
  default     = "eu-west-2"
}

variable "repository_name" {
  type        = string
  description = "Name of the ECR repository"
  default     = "network-automation-terraform-lab"
}