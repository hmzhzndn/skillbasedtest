import socket

def main():
    server_host = 'izani.synology.me'
    server_port = 8443

    data_to_send = '2021619532'

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect((server_host, server_port))
        print("Connected to the server.")

        client_socket.sendall(data_to_send.encode())

        reply = client_socket.recv(1024).decode()
        print("Received reply from the server:")
        print(reply)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
