#!/usr/bin/env bash

log() {
    echo "entry.sh: $1"
}

migrate() {
    log "running migrations"
    python manage.py migrate
}

log "running with settings module: $DJANGO_SETTINGS_MODULE"

case "$1" in
    "web")
	migrate
	log "launching web server"
	 0.0.0.0:8000
	;;
    "*")
	log "unknown command: $1"
	exit 1
	;;
esac
