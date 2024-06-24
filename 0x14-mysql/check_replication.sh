#!/usr/bin/env bash
# This script checks the status of MySQL replication

# Check slave status
mysql -u root -p -e "SHOW SLAVE STATUS\G;"
