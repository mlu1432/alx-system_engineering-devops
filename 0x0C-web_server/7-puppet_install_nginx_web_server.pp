# Setup New Ubuntu server with nginx

# Update system packages
exec { 'update system':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin/',
}

# Ensure nginx is installed
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

# Configure the main page
file {'/var/www/html/index.html':
  ensure  => 'file',
  content => '<html><body><h1>Hello World!</h1></body></html>',
  require => Package['nginx'],
}

# Configure Nginx to perform a 301 redirect from /redirect_me to LinkedIn
file_line { 'insert_redirect':
  path    => '/etc/nginx/sites-available/default',
  line    => 'rewrite ^/redirect_me https://www.linkedin.com/in/lucas-sekwati-723029bb/ permanent;',
  match   => '^rewrite ^/redirect_me',
  append_on_no_match => true,
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure nginx service is running and enabled
service {'nginx':
  ensure    => running,
  enable    => true,
  require   => File['/var/www/html/index.html'],
  subscribe => File_Line['insert_redirect'],
}
