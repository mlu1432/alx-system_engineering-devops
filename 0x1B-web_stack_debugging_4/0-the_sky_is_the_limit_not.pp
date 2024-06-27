# This manifest increases the amount of traffic an Nginx server can handle by setting the ULIMIT and restarting Nginx

# Increase the ULIMIT of the default file
file { 'fix-for-nginx':
  ensure  => 'file',
  path    => '/etc/default/nginx',
  content => inline_template('<%= File.read("/etc/default/nginx").gsub(/ULIMIT=".*"/, "ULIMIT=\\"-n 4096\\"") %>'),
  notify  => Exec['nginx-restart'],
}

# Restart Nginx
exec { 'nginx-restart':
  command     => 'service nginx restart',
  path        => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  refreshonly => true,
}

