#Configuration Management Tasks
#This repository contains Puppet manifests for a series of configuration management tasks. Each task is contained within its own manifest file, located in the 0x0A-configuration_management directory. The tasks are as follows:

- Task 0: Create a File
This task involves creating a file in /tmp using Puppet.

Requirements
File Path: /tmp/school
File Permission: 0744
File Owner: www-data
File Group: www-data
File Content: I love Puppet

- Task 1: Install a Package
This task involves installing Flask from pip3 using Puppet.

Requirements
Install Flask with version 2.1.0

- Task 2: Execute a Command
This task involves creating a manifest that kills a process named killmenow using the exec Puppet resource with pkill.

Requirements
Must use the exec Puppet resource.
Must use pkill.
