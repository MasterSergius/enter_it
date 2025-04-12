#include<stdio.h>


int main() {
    char message[] = "Hello world\n";
    int repeat = 5;

    for (int i=0; i<repeat; i++) {
        printf("%s", message);
    }
    return 0;
}
