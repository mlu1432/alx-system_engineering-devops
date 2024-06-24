#!/usr/bin/env bash
# This script creates a backup of the MySQL database

# Define variables
DB_USER="username"
DB_PASSWORD="password"
DB_NAME="database_name"
BACKUP_PATH="/path/to/backup"

# Create backup
mysqldump -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" > "$BACKUP_PATH/backup.sql"
