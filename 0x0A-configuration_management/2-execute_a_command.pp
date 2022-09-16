# Kill a process called killmenow

exec { 'kill process':
    command => 'pkill -f killmenow',
    path    => '/usr/bin'
}
