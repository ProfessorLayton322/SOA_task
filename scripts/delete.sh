#!/bin/bash

curl -H "Content-Type: application/json" -H "Authorization: $2" -d "{\"post_id\" : \"$1\"}" -X DELETE http://localhost:32206/api/post
