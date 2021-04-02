# Execute a command with Puppet.
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}
