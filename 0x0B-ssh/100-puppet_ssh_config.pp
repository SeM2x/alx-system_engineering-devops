# set up client SSH configuration file so that you can connect to a server without typing a password.
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => @(END),
Host web-01 100.25.163.188
    HostName 100.25.163.188
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
END
}
