#!/bin/bash

curl -H "Content-Type: application/json" -H "Authorization: $2" -d "{\"content\" : \"$1\"}" -X POST http://localhost:32206/api/post
