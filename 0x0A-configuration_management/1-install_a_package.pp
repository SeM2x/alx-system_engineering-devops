# installs flask from pip3
package { 'python3-pip':
  ensure => installed,
}

exec {'install_flask':
  command => '/usr/bin/pip install Flask==2.1.0'
}
