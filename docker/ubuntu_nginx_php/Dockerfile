# Download base image
FROM ubuntu:22.04

# Shell script or command
RUN apt update
RUN apt install -y nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/lib/nginx

VOLUME ["/data", "/etc/nginx/site-enabled", "/var/log/nginx"]

# 
WORKDIR /etc/nginx

CMD ["nginx"]

EXPOSE 80
EXPOSE 443