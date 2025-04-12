#include<stdio.h>
#include<string>

using namespace std;


class MessagePrinter {
public:
    string message;
    int repeat;

    void print_message() {
        for (int i=0; i<repeat; i++) {
            printf("%s", message.c_str());
        }
    }
};


int main() {
    MessagePrinter msg_printer;
    msg_printer.message = "Hello world\n";
    msg_printer.repeat = 5;

    msg_printer.print_message();
    return 0;
}
