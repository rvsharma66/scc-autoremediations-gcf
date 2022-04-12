prefix      = "secops-66degrees"
project_id  = "iac-admin-001"
region      = "us-central1"
region_zone = "us-central1-a"
location    = "US"
gcp_service_list = [
  "compute.googleapis.com",           # Compute Engine API
  "iam.googleapis.com",               # Identity and Access Management (IAM) API
  "iamcredentials.googleapis.com",    # IAM Service Account Credentials API
  "logging.googleapis.com",           # Stackdriver Logging API
  "monitoring.googleapis.com",        # Stackdriver Monitoring API
  "servicemanagement.googleapis.com", # Service Management API
  "serviceusage.googleapis.com",      # Service Usage API
  "sourcerepo.googleapis.com",        # Cloud Source Repositories API
  "sql-component.googleapis.com",     # Cloud SQL
  "sqladmin.googleapis.com",          # Cloud SQL
  "servicenetworking.googleapis.com", # Service Networking
  "storage-api.googleapis.com",       # Google Cloud Storage JSON API
  "storage-component.googleapis.com", # Cloud Storage
  "secretmanager.googleapis.com",     # Secret Manager
  "cloudbuild.googleapis.com"         # Cloud Build
]
# gce_ssh_user          = "root"
# machine_type          = "g1-small"
# gce_ssh_pub_key_file  = "id_rsa.pub"
# gce_ssh_priv_key_file = "id_rsa"
