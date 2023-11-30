# Nginx Puppet Manifest
class nginx_config {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    require    => Package['nginx'],
  }

  file { '/var/www/html/index.php':
    ensure  => file,
    content => '<?php echo "<p>Hello World</p>"; ?>',
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => 'server {
      listen 80 default_server;
      listen [::]:80 default_server;
      root /var/www/html;
      index index.php index.html index.htm;

      server_name _;

      location / {
        try_files $uri $uri/ =404;
      }

      location /redirect_me {
        return 301 http://example.com;
      }
    }',
    notify  => Service['nginx'],
  }
}

include nginx_config
