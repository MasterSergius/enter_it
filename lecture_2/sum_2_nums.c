#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    short int num1 = atoi(argv[1]);
    short int num2 = atoi(argv[2]);

    short int sum = num1 + num2;
    printf("%d\n", sum);

    return 0;
}
