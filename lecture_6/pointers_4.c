#include <stdio.h>


void greet(const char* name) {
    printf("Hello, %s!\n", name);
}

void bye(const char* name) {
    printf("Bye, %s!\n", name);
}

void say_something(void (*func)(const char*), const char* name) {
    func(name);
}

int main() {
    say_something(greet, "World");
    say_something(bye, "World");
    return 0;
}
