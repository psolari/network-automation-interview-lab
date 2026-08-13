variable "aws_region" {
  type        = string
  description = "AWS region to deploy resources into"
  default     = "eu-west-2"
}

variable "aws_profile" {
  type        = string
  description = "AWS CLI profile to use"
  default     = "personal"
}

variable "repository_name" {
  type        = string
  description = "Name of the ECR repository"
  default     = "network-automation-terraform-lab"
}