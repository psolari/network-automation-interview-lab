terraform {
  backend "s3" {
    bucket       = "network-automation-tfstate-122458452061"
    key          = "network-automation-lab/terraform.tfstate"
    region       = "eu-west-2"
    use_lockfile = true
    encrypt      = true
  }
}