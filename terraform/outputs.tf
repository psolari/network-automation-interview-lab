output "repository_url" {
  description = "URL of the ECR repository"
  value       = aws_ecr_repository.lab.repository_url
}

output "repository_arn" {
  description = "ARN of the ECR repository"
  value       = aws_ecr_repository.lab.arn
}

output "deployment_repository_url" {
  value = aws_ecr_repository.deployment.repository_url
}