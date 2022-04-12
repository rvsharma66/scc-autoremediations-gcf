/* -------------------------------------------------------------------------- */
/*                                 Global Vars                                */
/* -------------------------------------------------------------------------- */

variable "region" {
  description = "This is the cloud hosting region where your webapp will be deployed."
}

variable "prefix" {
  description = "This is the environment where your webapp is deployed. qa, prod, or dev"
}

variable "region_zone" {
  description = "This is the cloud hosting region's zone where your webapp will be deployed."
}

variable "project_id" {
  description = "The Project on which we want to work"
  type        = string
}

variable "gcp_service_list" {
  description = "Api to be enabled"
  type        = list(any)
}

variable "location" {
  description = "location of the resources."
  type        = string
}


/* --------------------------- End of Global Vars --------------------------- */
