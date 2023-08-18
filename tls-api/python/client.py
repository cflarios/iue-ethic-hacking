from socket import create_connection
from ssl import SSLContext, PROTOCOL_TLS_CLIENT


hostname='cflarios'
ip = '127.0.0.1'
port = 4443
context = SSLContext(PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem')

with create_connection((ip, port)) as client:
    with context.wrap_socket(client, server_hostname=hostname, ) as tls:
        
        print('\n\n')
        print(f'Conectado a: {hostname}:{port}\n')

        print(f'Usando: {tls.version()}\n')

        tls.sendall(b'Hello, Mr. Server!')
        data = tls.recv(1024)

        print(f'Mensaje del servidor: {data}')
        print('\n\n')