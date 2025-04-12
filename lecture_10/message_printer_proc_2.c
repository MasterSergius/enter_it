#include<stdio.h>


void print_message(char * message, int repeat) {
    for (int i=0; i<repeat; i++) {
        printf("%s", message);
    }
}

int main() {
    char message[] = "Hello world\n";
    int repeat = 5;

    print_message(message, repeat);
    return 0;
}

