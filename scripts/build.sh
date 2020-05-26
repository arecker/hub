#!/usr/bin/env bash

set -e

log() {
    echo "build.sh: $1" 1>&2;
}

docker_build() {
    docker buildx build \
	   --platform "linux/386,linux/amd64,linux/arm/v6,linux/arm/v7" \
	   --output "type=image,push=true" \
	   --tag "arecker/hub-${1}:latest" \
	   --file Dockerfile "dockerfiles/Dockerfile.${1}"
}

log "building $IMAGE_NAME"
docker_build "proxy"
docker_build "web"
