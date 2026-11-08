variable "aws_region" {
  description = "AWS deployment region"
  type        = string
  default     = "ap-southeast-2"
}

variable "vpc_id" {
  description = "Existing AWS VPC ID"
  type        = string
  default     = "vpc-0df455054f9dea637"
}
