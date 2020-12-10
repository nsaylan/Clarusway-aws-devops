provider "aws" {
    region = "us-east-1"
}

resource "aws_instance" "tf-example-ec2" {
    ami           = "ami-09d95fab7fff3776c"
    instance_type = "t2.micro" 
    key_name      = "First_key_pair"    #<pem file>
    tags = {
      Name = "tf-ec2"
  }
}

resource "aws_s3_bucket" "tf-example-s3" {
  bucket = "saylan-tf-test-bucket"
  acl    = "private"
}

output "tf-example-public-ip" {
  value = aws_instance.tf-example-ec2.public_ip
}

output "tf-example-s3-meta" {
  value = aws_s3_bucket.tf-example-s3
}