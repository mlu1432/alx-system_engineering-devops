# This manifest creates a file /tmp/school with specific owner, group, permissions and content

file { '/tmp/school':
  ensure  => 'present',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
