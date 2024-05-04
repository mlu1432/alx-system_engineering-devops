#!/usr/bin/pup
# Ensures that the 'killmenow' process is terminated if it is running
# Only runs if the 'killmenow' process is found
# Expects the command to return 0 to succeed
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
  returns => 0,
}
