#=============================================================
# Centos7, Apache2, PHP 7.4
#=============================================================

#Download base image Centos7
FROM centos:centos7

# LABEL about the custom image
LABEL maintainer="admin <admin@your-domain.com>"
LABEL title="Dev"
LABEL description="Centos 7 + Apache + php 7.4"
LABEL version="0.1"

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

#------------------------------------------------------------
# Define the ENV variable
#------------------------------------------------------------

ENV LANMG en_GB.UTF-8
ENV TZ=Asia/Seoul
ENV DEVELOPMENT 1
ENV php_conf /etc/php.ini


# -----------------------------------------------------------------------------
# Import the RPM GPG keys for Repositories
# -----------------------------------------------------------------------------
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

#------------------------------------------------------------
# Update Centos Software repository
#------------------------------------------------------------
RUN yum repolist \
&& yum -y install vi vim \
&& yum -y install httpd  \
&& yum -y install initscripts  \
&& yum -y update

# -----------------------------------------------------------------------------
# UTC Timezone & Networking
# -----------------------------------------------------------------------------
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime \
	&& echo "NETWORKING=yes" > /etc/sysconfig/network

# -----------------------------------------------------------------------------
# Apache 2.4.6
# -----------------------------------------------------------------------------
RUN	yum --setopt=tsflags=nodocs -y install \
	unzip \
	httpd \
	mod_ssl \
	&& rm -rf /var/cache/yum/* \
	&& yum clean all

# -----------------------------------------------------------------------------
# PHP 7.4.33
# -----------------------------------------------------------------------------
RUN yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm 
RUN yum -y install epel-release yum-utils
RUN yum-config-manager --enable remi-php74
RUN yum -y install php
RUN yum -y install php-fpm
RUN yum -y install  php-cli php-brotli php-intl php-gd php-gmp php-imap php-bcmath php-interbase php-json php-mbstring php-mysqlnd php-odbc php-opcache php-tidy php-pdo php-pdo-dblib php-pear php-pgsql php-process php-pecl-apcu php-pecl-geoip php-pecl-imagick php-pecl-hrtime php-pecl-json php-pecl-rar php-pecl-pq php-pecl-yaml php-pecl-zip php-mysql php-soap php-ldap php-firebird php-pdo-pgsql php-snmp php-xml php-xmlrpc php-xdebug && rm -rf /var/cache/yum/* && yum clean all

# -----------------------------------------------------------------------------
# SSH Client for SSH tunnel to dev MySQL Server, remove when no longer needed
# -----------------------------------------------------------------------------
#RUN yum -y install openssh-clients && rm -rf /var/cache/yum/* && yum clean all

# -----------------------------------------------------------------------------
# Configure Xdebug
# -----------------------------------------------------------------------------

COPY ./php.ini /etc/php.ini
COPY ./httpd.conf /etc/httpd/conf/httpd.conf
#COPY ./ssl.conf /etc/httpd/conf.d/ssl.conf
#COPY ./run.sh /run.sh

EXPOSE 80 8080 8081 8082 443

CMD /bin/bash

#["/usr/sbin/httpd", "-DFOREGROUND"]

ENTRYPOINT /usr/sbin/httpd -D FOREGROUND


