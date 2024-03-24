# set up client SSH configuration file so that you can connect to a server without typing a password.
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => @(END),
Host alx-web-01 54.237.91.249
    HostName 54.237.91.249
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
END
}
