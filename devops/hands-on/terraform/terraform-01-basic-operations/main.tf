provider "aws" {
// access_key = ""
// secret_key = ""
  region = "us-east-1"  
}
resource "aws_instance" "tf-ec2" {
  ami = "ami-0d5eff06f840b45e9"
  instance_type = "t2.micro"
  key_name = "First_key_pair"
  security_groups = ["tf-sec-gr"]

  tags = {
    Name = "Learn-Terraform"
  } 

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install -y yum-utils
              sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
              sudo yum -y install terraform         
              EOF
}

resource "aws_security_group" "tf-ec2-sec-gr" {
  name = "tf-sec-gr"

  tags = {
    "Name" = "terraform"
  }


  ingress {
    from_port = 22
    protocol = "tcp"
    to_port = 22
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port = 0
    protocol = "-1"
    to_port = 0
    cidr_blocks = ["0.0.0.0/0"]
  } 
}