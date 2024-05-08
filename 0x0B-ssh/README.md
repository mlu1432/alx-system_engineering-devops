# Server Configuration and SSH Setup

This repository contains scripts and configuration files for setting up SSH access to servers for administrative and testing purposes.

## Overview

The project involves creating secure SSH keys, configuring the SSH client, and ensuring servers accept key-based authentication without requiring passwords. The scripts automate the process of generating RSA key pairs, modifying SSH configuration files, and adding public keys to servers.

## Files

- `0-use_a_private_key`: Bash script that uses SSH to connect to a server using a specific private key.
- `1-create_ssh_key_pair`: Bash script that generates a 4096-bit RSA key pair with a passphrase.
- `2-ssh_config`: Custom SSH client configuration file to prevent password authentication and specify a private key.
- `100-puppet_ssh_config.pp`: Puppet manifest to automate the setup of the SSH client configuration to use key-based authentication.

## Tasks

### 0. Use a Private Key

A Bash script that connects to a server using the SSH protocol and authenticates using a private key stored at `~/.ssh/school`. This script demonstrates the basic use of SSH flags for connection.

**Usage**:

```bash
./0-use_a_private_key

### 1. Create an SSH Key Pair

Generates an RSA key pair secured with a passphrase. This script ensures the private key named school and its corresponding public key are created in the user's .ssh directory.

**Usage:

./1-create_ssh_key_pair

### 2. Client Configuration File
Updates the local SSH client configuration to use the private key ~/.ssh/school and disable password authentication. This is crucial for automating tasks and scripts that rely on SSH.

File: 2-ssh_config

### 3. Let Me In!
Adds a provided public key to the server's authorized keys file, allowing the key owner to SSH into the server under the ubuntu user. This task is essential for granting secure access to additional users.

Public Key: ssh-rsa AAAAB3...

### 4. Client Configuration File (w/ Puppet)
Utilizes Puppet to automate the changes required in the SSH client configuration file. This advanced task demonstrates the use of infrastructure as code for maintaining server configurations.

File: 100-puppet_ssh_config.pp
