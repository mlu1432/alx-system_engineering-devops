#!/usr/bin/env bash
# Puppet manifest to install and configure Nginx with a specific redirection and content

class nginx_setup {
  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Start and enable Nginx service
  service { 'nginx':
    ensure    => running,
    enable    => true,
    require   => Package['nginx'],
  }

  # Manage the Nginx configuration file
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    source  => 'puppet:///modules/nginx/default.conf', # Ensure this source file is correctly set up in your modules directory
    require => Package['nginx'],
    notify  => Service['nginx'], # Reload nginx service when the file changes
  }

  # Ensure the default web page displays "Hello World!"
  file { '/var/www/html/index.nginx-debian.html':
    ensure  => file,
    content => '<html><head><title>Hello World</title></head><body><h1>Hello World!</h1></body></html>',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}

# Declare the class
include nginx_setup

