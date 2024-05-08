# Puppet manifest to configure the SSH client

# Ensure the .ssh directory exists
file { '/home/ubuntu/.ssh':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

# Ensure the SSH config file exists
file { '/home/ubuntu/.ssh/config':
  ensure => file,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
  require => File['/home/ubuntu/.ssh'],  # Ensure directory is managed first
}

# Declare the private key to use
file_line { 'Declare identity file':
  path  => '/home/ubuntu/.ssh/config',
  line  => 'IdentityFile /home/ubuntu/.ssh/school',
  match => '^IdentityFile',
  replace => true,
  require => File['/home/ubuntu/.ssh/config'],  # Ensure config file is managed first
}

# Turn off password authentication
file_line { 'Turn off passwd auth':
  path    => '/home/ubuntu/.ssh/config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
  replace => true,
  require => File['/home/ubuntu/.ssh/config'],  # Ensure config file is managed first
}

# Turn off challenge-response authentication (optional)
file_line { 'Turn off challenge-response auth':
  path    => '/home/ubuntu/.ssh/config',
  line    => 'ChallengeResponseAuthentication no',
  match   => '^ChallengeResponseAuthentication',
  replace => true,
  require => File['/home/ubuntu/.ssh/config'],  # Ensure config file is managed first
}
