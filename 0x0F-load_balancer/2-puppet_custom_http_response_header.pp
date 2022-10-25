# Puppet manifest to install nginx and configure the server
package { 'nginx':
  ensure => installed,
}

file_line { 'Redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'setHeader':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  after  => 'include /etc/nginx/sites-enabled/*;',
  line   => 'add_header X-Served-By $HOSTNAME;',
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
