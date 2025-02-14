#include <stdio.h>


struct Credentials {
    char username[50];
    char password[50];
};


int main() {
    struct Credentials admin = {
        "admin",
        "SuperSecretPass*123"
    };

    char * struct_ptr = (char *)&admin;

    printf("Struct: %s\n", struct_ptr + 50);
    return 0;
}
