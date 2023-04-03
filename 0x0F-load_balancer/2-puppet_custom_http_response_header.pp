# Install Nginx web server
class { 'nginx': }

# Define custom HTTP header
$custom_header_name = 'X-Served-By'
$custom_header_value = $::hostname

# Add custom HTTP header to Nginx configuration
file { '/etc/nginx/conf.d/custom-http-headers.conf':
  content => "add_header $custom_header_name \"$custom_header_value\";",
  mode    => '0644',
  notify  => Service['nginx'],
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  hasrestart => true,
}
