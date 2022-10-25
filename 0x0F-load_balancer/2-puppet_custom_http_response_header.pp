# Puppet manifest to install nginx and configure the server
exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
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

file_line { 'set_header':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  after  => 'include /etc/nginx/sites-enabled/*;',
  line   => '\n\tadd_header X-Served-By $HOSTNAME;\n',
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
