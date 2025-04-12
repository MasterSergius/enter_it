#include<stdio.h>


void print_message(char * message, int repeat) {
    if (repeat == 0) return;

    printf("%s", message);
    print_message(message, repeat-1);
}

int main() {
    char message[] = "Hello world\n";
    int repeat = 5;

    print_message(message, repeat);
    return 0;
}
