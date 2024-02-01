#!/usr/bin/env bash
# Sets up a web server for the deployment of web_static

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "Hello World!" > /data/web_static/releases/test/index.html
ls -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

sed -i "61i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default

service nginx restart
