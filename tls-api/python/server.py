from socket import socket, AF_INET, SOCK_STREAM
from ssl import SSLContext, PROTOCOL_TLS_SERVER


ip = '0.0.0.0'
port = 4443
context = SSLContext(PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')

with socket(AF_INET, SOCK_STREAM) as server:
    server.bind((ip, port))
    server.listen(1)
    with context.wrap_socket(server, server_side=True) as tls:
        
        print('\n\n')
        print(f'Servidor corriendo en: {ip}:{port}\n')
        
        connection, address = tls.accept()
        tls_version = connection.version()

        print(f'Conectado por: {address}\n')

        data = connection.recv(1024)

        print(f'Mensaje del cliente: {data}\n')
        print(f'Usando: {tls_version}')

        connection.sendall(b"Welcome back, sir")
        print('\n\n')