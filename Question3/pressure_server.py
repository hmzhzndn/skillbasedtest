import socket

def convert_to_atm(pressure_bar):
    return pressure_bar / 1.01325

def main():
    server_host = '192.168.174.128'
    server_port = 8443

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((server_host, server_port))
    server_sock.listen(1)

    print("server is listening for incoming connections...")
    client_sock, client_addr = server_sock.accept()
    print("connection established with:", client_addr)

    while True:
        try:
            data = client_sock.recv(1024).decode()
            if not data:
                break

            pressure_bar = float(data)
            pressure_atm = convert_to_atm(pressure_bar)

            client_sock.send(str(pressure_atm).encode())
        except ValueError:
            client_sock.send("invalid input. Please enter a valid pressure value in bar.".en>
        except Exception as e:
            print("error occurred:", e)
            break

    print("connectionn closed.")
    client_sock.close()
    server_sock.close()

if __name__ == "__main__":
    main()
