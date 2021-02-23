#!/usr/bin/env bash

DATABASE=`printenv DATABASE || echo /srv/db.sqlite3`

function main() {
  if [ ! -e ${DATABASE} ]; then
    init
  fi
  run
}

function init() {
  DATABASE=${DATABASE} poetry run poe migrate
}

function run() {
  DATABASE=${DATABASE} poetry run poe runserver
}

main
