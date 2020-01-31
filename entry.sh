#!/usr/bin/env bash

log() {
    echo "entry.sh: $1"
}

migrate() {
    log "running migrations"
    python manage.py migrate
}

validate_proxy_vars() {
    log "validating environment variables"
    if [[ -z "$UPSTREAM_DNS" ]]; then
	echo "UPSTREAM_DNS not set" 1>&2
	exit 1
    fi

    if [[ -z "$UPSTREAM_HOSTNAME" ]]; then
	echo "UPSTREAM_HOSTNAME not set" 1>&2
	exit 1
    fi
}

sub_proxy_vars() {
    log "subbing {{UPSTREAM_HOSTNAME}} with \"$UPSTREAM_HOSTNAME\""
    sed -i "s/{{UPSTREAM_HOSTNAME}}/$UPSTREAM_HOSTNAME/g" /etc/nginx/nginx.conf
    log "subbing {{UPSTREAM_DNS}} with \"$UPSTREAM_DNS\""
    sed -i "s/{{UPSTREAM_DNS}}/$UPSTREAM_DNS/g" /etc/nginx/nginx.conf
}

case "$1" in
    "proxy")
	validate_proxy_vars
	sub_proxy_vars
	log "validating nginx config"
	nginx -t
	log "starting nginx"
	nginx -g "daemon off;"
	;;
    "web")
	log "running with settings module: $DJANGO_SETTINGS_MODULE"
	migrate
	log "launching web server"
	gunicorn -b 0.0.0.0:8000 hub.wsgi
	;;
    "*")
	log "unknown command: $1"
	exit 1
	;;
esac
