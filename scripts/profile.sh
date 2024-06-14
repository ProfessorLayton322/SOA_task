#!/bin/bash

curl -H "Content-Type: application/json" -H "Authorization: $1" -X GET http://localhost:32206/api/profile
