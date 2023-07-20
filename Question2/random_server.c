#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <time.h> // Add this header for the time() function

int main() {
    int server_sock, client_sock;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_addr_len = sizeof(client_addr);
    int random_number;

    server_sock = socket(AF_INET, SOCK_STREAM, 0);
    if (server_sock == -1) {
        perror("creating socket error");
        exit(EXIT_FAILURE);
    }

    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(8443); // Use port 8443 for communication

    if (bind(server_sock, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        perror("socket binding error");
        close(server_sock);
        exit(EXIT_FAILURE);
    }

    if (listen(server_sock, 1) == -1) {
        perror("listening to connection error");
        close(server_sock);
        exit(EXIT_FAILURE);
    }

    printf("Server is listening...\n");

    client_sock = accept(server_sock, (struct sockaddr*)&client_addr, &client_addr_len);
    if (client_sock == -1) {
        perror("accepting client connection error");
        close(server_sock);
        exit(EXIT_FAILURE);
    }

    srand(time(NULL));
    random_number = rand() % 900 + 100;

    send(client_sock, &random_number, sizeof(random_number), 0);

    printf("Random number %d sent to the client.\n", random_number);

    close(client_sock);
    close(server_sock);
    return 0;
}
