exec { 'kill process':
    command => 'pkill -f killmenow'
    path    => '/usr/bin'
}
