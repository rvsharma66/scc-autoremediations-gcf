resource "random_string" "lower" {
  length  = 4
  upper   = false
  lower   = true
  number  = false
  special = false
}

locals {
  gcf = {
    "gcf-01" = { name = "${var.prefix}-${random_string.lower.result}-firewall-remediation", path = "../gcf/firewall/", dest = "../tmp/firewall.zip", description = "firewall auto remediation by 66Degrees.", resource = "projects/iac-admin-001/topics/traininglabs-scc-alerts", event_type = "google.pubsub.topic.publish"
    },
  }
}

# Enable services in newly created GCP Project.
resource "google_project_service" "gcp_services" {
  count                      = length(var.gcp_service_list)
  project                    = var.project_id
  service                    = var.gcp_service_list[count.index]
  disable_dependent_services = true
}

resource "google_storage_bucket" "bucket" {
  project  = var.project_id
  name     = "${var.prefix}-${random_string.lower.result}-bucket"
  location = var.location
}

/* -------------------------------------------------------------------------- */
/*                                GCF Firewall                                */
/* -------------------------------------------------------------------------- */

data "archive_file" "src" {
  for_each = local.gcf

  type        = "zip"
  source_dir  = each.value.path
  output_path = each.value.dest
}

resource "google_storage_bucket_object" "archive" {
  for_each = local.gcf

  name   = "firewall.zip"
  bucket = google_storage_bucket.bucket.name
  source = data.archive_file.src[each.key].output_path
}

resource "google_cloudfunctions_function" "function" {
  for_each = local.gcf

  project             = var.project_id
  region              = var.region
  name                = each.value.name
  description         = each.value.description
  runtime             = "python38"
  available_memory_mb = 512

  source_archive_bucket = google_storage_bucket.bucket.name
  source_archive_object = google_storage_bucket_object.archive[each.key].name

  event_trigger {
    event_type = each.value.event_type
    resource   = each.value.resource
  }

  timeout     = 80
  entry_point = "entrypoint"

  labels = {
    maintainer = "66degrees"
  }

  environment_variables = {
    action      = "replace"                      // either "disable" or "replace"disable
    trusted_ips = "192.168.0.32,192.168.1.23/32" // set of IPs that are trusted to your organization, will only work with action "replace".
  }

}
