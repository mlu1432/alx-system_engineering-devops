# This Puppet manifest installs the missing PHP module and ensures Apache is running.

package { 'php-mysql':
  ensure => installed,
}

exec { 'stop_conflicting_process':
  command => '/usr/bin/sudo /usr/sbin/fuser -k 80/tcp',
  onlyif  => '/usr/bin/sudo /usr/bin/lsof -i :80',
  before  => Service['apache2'],
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Package['php-mysql'],
}
