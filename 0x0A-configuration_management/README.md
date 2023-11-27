# Configuration Management with Puppet

This repository contains Puppet manifests for various operational requirements as part of the system engineering and DevOps practice. The manifests are designed to be used with Puppet to automate the configuration management of servers.

## Files in the Repository

### 0-create_a_file.pp

A Puppet manifest that creates a file with specific properties.

**Requirements:**

- File path: `/tmp/school`
- File permission: `0744`
- File owner: `www-data`
- File group: `www-data`
- File content: `I love Puppet`

To run the manifest:

