#!/bin/bash

curl -H "Content-Type: application/json" -d "{\"username\": \"$1\", \"password\" : \"$2\"}" -X POST http://localhost:32206/api/login
