#!/usr/bin/env bash
# This script sets up the MySQL slave server

# Install MySQL 8.0
sudo apt-get update
sudo apt-get install -y mysql-server

# Configure MySQL
sudo bash -c 'cat <<EOF > /etc/mysql/mysql.conf.d/mysqld.cnf
[mysqld]
server-id = 2
relay_log = /var/log/mysql/mysql-relay-bin.log
EOF'

# Restart MySQL
sudo service mysql restart

# Set up replication
mysql -u root -p -e "
CHANGE MASTER TO
	MASTER_HOST='master_ip',
	MASTER_USER='replica_user',
	MASTER_PASSWORD='password',
	MASTER_LOG_FILE='mysql-bin.000001',
	MASTER_LOG_POS=log_position;
START SLAVE;
"

# Show slave status
mysql -u root -p -e "SHOW SLAVE STATUS\G;"
