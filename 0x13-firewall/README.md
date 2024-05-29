# 0x13-firewall

This project focuses on configuring the `ufw` firewall on an Ubuntu server (`web-01`) to enhance security by blocking unnecessary traffic and setting up port forwarding.

## Tasks

### 0. Block All Incoming Traffic but Allow SSH, HTTP, and HTTPS

**Objective:**
- Configure `ufw` so that it blocks all incoming traffic except for the following TCP ports:
  - 22 (SSH)
  - 80 (HTTP)
  - 443 (HTTPS)

**Requirements:**
- The configuration must be applied to `web-01`. You can also apply it to `lb-01` and `web-02`, but it will not be checked.

**Steps:**
1. **Install `ufw`:**
   ```sh
   sudo apt-get update
   sudo apt-get install ufw

