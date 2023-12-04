#!/usr/bin/evn bash
# configuration file to allow puppet to make changes
file { 'ect/ssh/ssh_cofig':
	ensure => present,
content =>"
	#ssh client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
