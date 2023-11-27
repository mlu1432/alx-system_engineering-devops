# This manifest creates an executable script named 'killmenow' in the /root directory
file { '/root/killmenow':
  ensure  => 'file',                    # Ensure the file resource exists
  mode    => '0755',                    # Make sure the script is executable
  content => "#!/bin/bash\nwhile true; do\n  sleep 2\ndone", # Script content
  owner   => 'root',                    # Set the file owner to root
  group   => 'root',                    # Set the file group to root
}
