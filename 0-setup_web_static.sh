#!/usr/bin/env bash
# This script sets up a web server for the deployment of web_static.

# Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    apt-get -y update
    apt-get -y install nginx
fi

# Create necessary directories if they don't exist
web_static_dir="/data/web_static"
web_static_releases="${web_static_dir}/releases"
web_static_shared="${web_static_dir}/shared"
web_static_test="${web_static_releases}/test"

mkdir -p "$web_static_dir" "$web_static_releases" "$web_static_shared" "$web_static_test"

# Create a fake HTML file for testing
echo "<html><head></head><body>Holberton School</body></html>" > "${web_static_test}/index.html"

# Create or update the symbolic link
current_symlink="${web_static_dir}/current"
if [ -h "$current_symlink" ]; then
    unlink "$current_symlink"
fi
ln -s "$web_static_test" "$current_symlink"

# Give ownership to the ubuntu user and group
chown -R ubuntu:ubuntu "/data/"

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
config_alias="location /hbnb_static/ {\n\talias ${web_static_dir}/current/;\n}\n"

if ! grep -q "location /hbnb_static/" "$nginx_config"; then
    sed -i "/server_name _;/a $config_alias" "$nginx_config"
fi

# Restart Nginx
service nginx restart
