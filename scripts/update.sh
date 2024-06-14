#!/bin/bash

JSON_ARGS=$(cat "$1")
curl -H "Content-Type: application/json" -H "Authorization: $2" -d "$JSON_ARGS" -X PUT http://localhost:32206/api/update
