##0x13. Firewall project

**For `0-block_all_incoming_traffic_but` README.md:**

```
# UFW Firewall Configuration

This document explains how to configure UFW (Uncomplicated Firewall) to block all incoming traffic except for SSH (port 22), HTTPS (port 443), and HTTP (port 80).

## Steps to configure UFW

1. First, install UFW if it is not already installed:
   ```
   sudo apt-get install ufw
   ```

2. Set UFW to block all incoming traffic by default:
   ```
   sudo ufw default deny incoming
   ```

3. Allow incoming SSH connections:
   ```
   sudo ufw allow 22/tcp
   ```

4. Allow incoming HTTPS connections:
   ```
   sudo ufw allow 443/tcp
   ```

5. Allow incoming HTTP connections:
   ```
   sudo ufw allow 80/tcp
   ```

6. Enable the UFW firewall:
   ```
   sudo ufw enable
   ```

7. Check the status of UFW to ensure the rules are applied:
   ```
   sudo ufw status
   ```
```

**For `100-port_forwarding` README.md:**

```
# Port Forwarding with UFW

This document provides instructions on how to configure port forwarding using UFW so that traffic to port 8080/TCP is redirected to port 80/TCP.

## Steps to configure port forwarding

1. Edit the UFW before.rules file to add the following nftables rules:
   ```
   sudo nano /etc/ufw/before.rules
   ```

2. Add the following lines to the file, before the `*filter` line:
   ```
   *nat
   :PREROUTING ACCEPT [0:0]
   -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
   COMMIT
   ```

3. Save and close the file.

4. Reload UFW to apply the changes:
   ```
   sudo ufw reload
   ```

5. Verify that the port forwarding rule has been applied:
   ```
   sudo ufw status verbose
   ```

By following these steps, traffic to port 8080/TCP will be redirected to port 80/TCP, allowing services listening on port 80 to be accessible via port 8080 as well.
```

Please replace the placeholder text with actual commands if necessary, and make sure to test these configurations in your environment before publishing.

**From Claude**  Here are the ufw commands to configure port forwarding from 8080/TCP to 80/TCP on web-01:

```
