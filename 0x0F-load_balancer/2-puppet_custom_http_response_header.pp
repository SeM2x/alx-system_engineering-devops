# Configures a brand new Ubuntu machine
package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n"
}

exec {'redirect':
  command => "/usr/bin/sed -i '24i\\	rewrite ^/redirect_me localhost permanent;' /etc/nginx/sites-available/default"
}

exec {'add_header':
  environment => ["HOST=${hostname}"],
  command => '/usr/bin/sed -i "25i\\        add_header X-Served-By \"$HOST\";" /etc/nginx/sites-available/default'
}

exec {'service':
  command => '/usr/sbin/service nginx start'
}
