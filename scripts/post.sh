#!/bin/bash

curl -H "Content-Type: application/json" -H "Authorization: $1" -d '{"content" : "Sample text"}' -X POST http://localhost:32206/api/post
