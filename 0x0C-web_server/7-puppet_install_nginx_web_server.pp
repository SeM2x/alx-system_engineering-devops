#!/usr/bin/env bash
# script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself
package { 'nginx':
	ensure => installed,
}

file { '/var/www/html/index.html': 
	ensure  => present,
	content => "Hello World!\n"
}

exec {'sed':
	command => "/usr/bin/sed -i '24i\\	rewrite ^/redirect_me localhost permanent;' /etc/nginx/sites-available/default"
}

exec {'service':
	command => '/usr/sbin/service nginx start'
}
