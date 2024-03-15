# Networking Basics 2

This collection of Bash scripts is designed to explore and demonstrate various networking. From displaying active IP addresses to setting up a listener on a specific port, these scripts serve as practical tools for understanding network operations.

## Scripts

### 0-change_your_home_IP

This script modifies the `/etc/hosts` file to:

- Resolve `localhost` to `127.0.0.2`.
- Resolve `facebook.com` to `8.8.8.8`.

### 1-show_attached_IPs

This script displays all active IPv4 addresses on the machine, including the localhost IP.

### 100-port_listening_on_localhost

Sets up a listener on port 98 on localhost. It can receive and display text sent to this port, demonstrating simple socket communication.