output "security_group_id" {
  description = "ID of the AWS DevOps Security Group"
  value       = aws_security_group.devops_sg.id
}

output "security_group_name" {
  description = "Name of the Security Group"
  value       = aws_security_group.devops_sg.name
}

output "vpc_id" {
  description = "VPC ID"
  value       = aws_security_group.devops_sg.vpc_id
}

