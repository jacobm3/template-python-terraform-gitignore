terraform {
  backend "s3" {
    bucket = "jm3-state"
    key    = "project-name"
    region = "us-east-1"
    dynamodb_table  = "jm3-state"
  }
}
