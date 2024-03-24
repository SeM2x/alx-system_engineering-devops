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
