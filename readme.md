# Auto Remediating GCP misconfigurations.

### Deployment

```bash
cd ../infra/
terraform init
terraform plan
terraform apply
terraform destroy
```

| Resources                                   | Findings                            |                             Tier                             |      Finding       | Remediation        | Action                      |
| ------------------------------------------- | ----------------------------------- | :----------------------------------------------------------: | :----------------: | ------------------ | --------------------------- |
| **Compute image vulnerability findings**    | PUBLIC_COMPUTE_IMAGE                | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
| **Compute instance vulnerability findings** | PUBLIC_IP_ADDRESS                   | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
| **Container vulnerability findings**        | LEGACY_AUTHORIZATION_ENABLED        | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
| **Container vulnerability findings**        | WEB_UI_ENABLED                      | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
| **Dataproc vulnerability findings**         | DATAPROC_IMAGE_OUTDATED             | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
| **Dataproc vulnerability findings**         | PUBLIC_DATASET                      | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
| **Firewall vulnerability findings**         | OPEN_CISCOSECURE_WEBSM_PORT         | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :white_check_mark: | Disable OR trusted IPs only |
| **Firewall vulnerability findings**         | OPEN_DIRECTORY_SERVICES_PORT        | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :white_check_mark: | Disable OR trusted IPs only |
| **Firewall vulnerability findings**         | OPEN_FIREWALL                       | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :white_check_mark: | Disable OR trusted IPs only |
| **Firewall vulnerability findings**         | OPEN_RDP_PORT                       | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :white_check_mark: | Disable OR trusted IPs only |
| **Firewall vulnerability findings**         | OPEN_SSH_PORT                       | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :white_check_mark: | Disable OR trusted IPs only |
| **Firewall vulnerability findings**         | OPEN_TELNET_PORT                    | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :white_check_mark: | Disable OR trusted IPs only |
| **IAM vulnerability findings**              | NON_ORG_IAM_MEMBER                  | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
| **IAM vulnerability findings**              | OPEN_GROUP_IAM_MEMBER Kindly Please | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
| **Multi-factor authentication findings**    | MFA_NOT_ENFORCED                    | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
| **SQL vulnerability findings**              | PUBLIC_SQL_INSTANCE                 | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
| **SQL vulnerability findings**              | SSL_NOT_ENFORCED                    | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
| **Storage vulnerability findings**          | PUBLIC_BUCKET_ACL                   | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
| **Storage vulnerability findings**          | PUBLIC_LOG_BUCKET                   | [Premium or Standard](https://cloud.google.com/security-command-center/pricing#standard-tier) | :white_check_mark: | :x:                | :x:                         |
