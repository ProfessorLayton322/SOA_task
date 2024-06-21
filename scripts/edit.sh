#!/bin/bash

curl -H "Content-Type: application/json" -H "Authorization: $3" -d "{\"new_content\" : \"$2\", \"post_id\" : \"$1\"}" -X PUT http://localhost:32206/api/post
