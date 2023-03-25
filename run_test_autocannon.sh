#!/bin/bash
servers=("http://0.0.0.0:5000" "http://0.0.0.0:5001" "http://0.0.0.0:3000")

for server in "${servers[@]}"
do
  autocannon "$server" -d 20 -c 1000 
done