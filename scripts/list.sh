#!/bin/bash

curl -H "Content-Type: application/json" -H "Authorization: $3" -d "{\"page_size\" : \"$1\", \"offset\" : \"$2\"}" -X GET http://localhost:32206/api/list
