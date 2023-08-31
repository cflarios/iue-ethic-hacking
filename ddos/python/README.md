# Simple DoS Script

**Disclaimer**: This guide is for educational purposes only. Unauthorized and malicious use of this script to flood requests to a server is illegal and unethical.

This is a simple DoS script written in Python that sends HTTP GET requests to a target server.

## Prerequisites

- Python 3

## Usage

1. Clone this repository or download the `dos.py` and `ddos` directory.

2. Start a simple HTTP server to act as the target:

   ```bash
   python -m http.server 5500
   ```

3. In a separate terminal, navigate to the directory containing the ddos.py script.

4. Run the DoS script with the following command:

    ```bash
    python dos.py <target> <port> <path> <num_threads>
    ```
    Replace the placeholders with the following values:

    <**target**>: The IP address or hostname of the target server.

    <**port**>: The port on which the target server is running.

    <**path**>: The path to the HTML file on the target server.

    <**num_threads**>: The number of threads (simultaneous requests) to use.

    For example:

    ```bash
    python dos.py 127.0.0.1 5500 ddos/python/index.html 10
    ```

5. The script will start sending HTTP requests to the specified target. It will display whether the requests were successfully sent or if an error occurred. If an error occurs in any thread, the script will stop and display an error message.

6. Once the script finishes, it will display whether the attack was successful or not.

**Note**: Be responsible and only use this script on servers you have permission to test on. Unauthorized use of this script is illegal and unethical.