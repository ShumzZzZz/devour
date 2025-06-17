variable "default_project_tags" {
  description = "Default project tags"
  type        = map(string)
  default = {
    Environment = "Dev"
    Project     = "Devour Feature Store"
    Team        = "MLE-Shumin"
  }
}

variable "environment" {
  description = "Environment, either dev or prod"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "prod"], var.environment)
    error_message = "Environment must be either dev or prod."
  }
}

variable "containerd_version" {
  description = "Containerd version"
  type        = string
  default     = "2.0.4"
}

variable "runc_version" {
  description = "Runc version"
  type        = string
  default     = "1.2.6"
}

variable "cni_plugin_version" {
  description = "cni plugin version"
  type        = string
  default     = "1.6.2"
}

variable "tigera_calico_version" {
  description = "tigera calico version"
  type        = string
  default     = "3.29.3"
}

variable "key_pair_name" {
  description = "key pair name"
  type        = string
  default     = "shumin-test"
}
