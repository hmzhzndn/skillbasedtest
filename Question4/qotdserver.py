import socket
import threading
import random

quotes = [
    "if you expect disappoinment, then you'll never get disappointed",
    "anyone can wear the mask",
    "everyone keeps telling me how my story supposed to go, nah imma do my own thing",
    "i harness the harnessed",
    "fire in the hole!",
    "sejauh mana pemandangan boleh pergi, titik perubahan adalah Ipoh; datuk hamzah, Indiana Jones Perak, Ipoh, Perak",
    "destinasi sebenar bukanlah yang ada di hadapan namun apa yang di belakang; datuk hamzah"
]

def handle_client(client_sock):
    quote = random.choice(quotes)

    client_sock.send(quote.encode())
    client_sock.close()

def main():
    host = '192.168.174.128'
    port = 8888

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind((host, port))
    server_sock.listen(5)

    print("server is listening on port 8888...")

    while True:
        try:
            client_sock, client_addr = server_sock.accept()
            print("accepted connection from:", client_addr)

            client_hand = threading.Thread(target=handle_client, args=(client_sock,))
            client_hand.start()
        except KeyboardInterrupt:
            print("server shutting down...")
            break
        except Exception as e:
            print("error occurred:", e)

    server_sock.close()

if __name__ == "__main__":
    main()
