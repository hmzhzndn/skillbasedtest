#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int client_sock;
    struct sockaddr_in server_addr;
    int random_number;

    client_sock = socket(AF_INET, SOCK_STREAM, 0);
    if (client_sock == -1) {
        perror("creating socket error");
        exit(EXIT_FAILURE);
    }

    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8443); 

    if (inet_pton(AF_INET, "192.168.174.128", &server_addr.sin_addr) <= 0) {
        perror("invalid address");
        close(client_sock);
        exit(EXIT_FAILURE);
    }

    if (connect(client_sock, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        perror("connecting to server error");
        close(client_sock);
        exit(EXIT_FAILURE);
    }

    recv(client_sock, &random_number, sizeof(random_number), 0);

    printf("Received random number from server: %d\n", random_number);

    close(client_sock);
    return 0;
}
