terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_security_group" "devops_sg" {
  name        = "aws-devops-terraform-sg"
  description = "Security group created using Terraform"
  vpc_id      = var.vpc_id

  ingress {
    description = "Allow application traffic inside VPC"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["172.31.0.0/16"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "aws-devops-terraform-sg"
    Environment = "Dev"
    ManagedBy   = "Terraform"
  }
}
