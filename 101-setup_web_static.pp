# Puppet Manifest for Setting up a Web Server and Deploying web_static

# Update package list
exec { 'update_package_list':
  command     =>  '/usr/bin/apt-get update',
  refreshonly => true,
}

# Install Nginx if not already installed
package { 'nginx':
  ensure  =>  'installed',
  require =>  Exec['update_package_list'],
}

# Create necessary directories if they don't exist
file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Create or update the symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true,
}

# Give ownership to the ubuntu user and group
file { '/data':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration
file_line { 'web_static_alias':
  path => '/etc/nginx/sites-available/default',
  line => 'location /hbnb_static/ { alias /data/web_static/current/; }',
}

# Restart Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File_line['web_static_alias'],
}
