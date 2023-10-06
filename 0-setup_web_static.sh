#!/usr/bin/env bash
# A bash script that sets up my wwb servers for the deployment
# of web_static

# Ensuring that the programme always exit succesful
trap 'exit 0' ERR


# Installing Nginx
sudo apt-get update -y
sudo apt-get install nginx -y

# Creating necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Creating fake HTML file for testing Nginx configuration
content="<html>
  <head></head>
  <body>XimeonLeo under construction</body>
</html>"

echo "$content"| sudo tee /data/web_static/releases/test/index.html

# Deleting the initial sybolic link
rm -rf /data/web_static/current

# Creating new symbolic link to "/data/web_static/releases/test/"
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Giving ownership to /data/ directory to ubuntu user
sudo chown -Rh ubuntu:ubuntu /data/

# Configuring Nginx
config_file="/etc/nginx/sites-available/default"

echo 'Hello World' | sudo tee /var/www/html/index.html > /dev/null
replacement="server_name _;\n\trewrite ^\/redirect_me https:\/\/www.google.com permanent;"
sudo sed -i "s/server_name _;/$replacement/" $config_file

echo "Ceci n'est pas une page" | sudo tee /usr/share/nginx/html/404.html
newlines="\\\terror_page 404 /404.html;\n\tlocation = /404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}"
sudo sed -i "27i $newlines" $config_file

sudo sed -i "50i\\\t\tadd_header X-Served-By $HOSTNAME;" $config_file

sudo sed -i '/^server {/a \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}' $config_file

# Restarting Nginx
sudo service nginx restart
