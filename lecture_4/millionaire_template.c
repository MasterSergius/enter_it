#include <stdio.h>

char choice;

int main() {
    printf("London is a capital of ...\n");
    printf("a - Canada\n");
    printf("b - Great Britain\n");
    printf("c - Luxembourg\n");
    printf("d - Australia\n");
    printf("\nYour choice: ");
    scanf(" %c", &choice);
    if (choice == 'b') {
        printf("Correct\n");
    } else {
        printf("Wrong\n");
    }
    return 0;
}
