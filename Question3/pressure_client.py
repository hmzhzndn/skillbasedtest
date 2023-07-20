import socket

def main():
    server_host = '192.168.174.128'
    server_port = 8443

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_sock.connect((server_host, server_port))

        while True:
            pressure_input = input("enter pressure value in bar (q to quit): ")

            if pressure_input.lower() == 'q':
                break

            try:
                pressure_bar = float(pressure_input)
                client_sock.send(str(pressure_bar).encode())

                response = client_sock.recv(1024).decode()
                print("pressure in atmosphere-standard:", response)
            except ValueError:
                print("invalid input. Please enter a valid pressure value in bar.")
            except Exception as e:
                print("error occurred:", e)

    except ConnectionRefusedError:
        print("error: connection refused. please ensure the server is running.")
    except Exception as e:
        print("error occurred:", e)
    finally:
        client_sock.close()

if __name__ == "__main__":
    main()
