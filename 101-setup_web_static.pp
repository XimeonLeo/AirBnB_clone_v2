# install and configure nginx
exec { 'install_nginx':
  command     => '/usr/bin/apt-get update',
  onlyif      => '/usr/bin/which nginx',
}
-> package { 'nginx':
  ensure => installed,
}
-> exec { 'path1'':
  command => '/usr/bin/mkdir -p "/data/web_static/releases/test/" "/data/web_static/shared/"',
}
-> exec { 'run_1':
  command => '/usr/bin/echo "Hi!" | sudo tee /data/web_static/releases/test/index.html > /dev/null',
}
-> exec { 'run_2':
  command => '/usr/bin/rm -rf /data/web_static/current',
}
-> exec { 'run_3':
  command => '/usr/bin/ln -s /data/web_static/releases/test/ /data/web_static/current',
}
-> exec { 'chown':
  command => '/usr/bin/chown -R ubuntu:ubuntu /data/',
}
-> file_line { 'alias':
  path     => '/etc/nginx/sites-available/default',
  match    => '^server {',
  line     => "server {\n\tlocation /hbnb_static {alias /data/web_static/current/;index index.html;}",
  multiple => false,
}
-> exec { 'reatart':
  command => '/usr/sbin/service nginx restart',
}
