#!/usr/bin/env bash
# A bash script that sets up my wwb servers for the deployment
# of web_static

# Installing Nginx
sudo apt-get update -y
sudo apt-get install nginx -y

# Creating necessary directories
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Creating fake HTML file for testing Nginx configuration
echo "
<h1>Welcome to XimeonLeo</h1>
" > /data/web_static/releases/test/index.html

# Creating symbolic link to "/data/web_static/releases/test/"
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Giving ownership to /data/ directory to ubuntu user
sudo chown -Rh ubuntu:ubuntu /data

# Restarting Nginx
sudo service nginx restart
