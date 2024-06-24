#!/usr/bin/env bash
# This script sets up the MySQL master server

# Install MySQL 8.0
sudo apt-get update
sudo apt-get install -y mysql-server

# Configure MySQL
sudo bash -c 'cat <<EOF > /etc/mysql/mysql.conf.d/mysqld.cnf
[mysqld]
server-id = 1
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = your_database_name
EOF'

# Restart MySQL
sudo service mysql restart

# Create replication user
mysql -u root -p -e "CREATE USER 'replica_user'@'%' IDENTIFIED BY 'password';"
mysql -u root -p -e "GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';"
mysql -u root -p -e "FLUSH PRIVILEGES;"

# Show master status
mysql -u root -p -e "SHOW MASTER STATUS;"
