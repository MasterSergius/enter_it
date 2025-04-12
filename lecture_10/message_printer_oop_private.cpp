#include<stdio.h>
#include<string>

using namespace std;


class MessagePrinter {
private:
    string message;
    int repeat;

public:
    MessagePrinter(string msg, int rpt) {
        message=msg;
        repeat=rpt;
    }

    void print_message() {
        for (int i=0; i<repeat; i++) {
            printf("%s", message.c_str());
        }
    }
};


int main() {
    MessagePrinter msg_printer("Hello world\n", 5);

    msg_printer.print_message();
    return 0;
}
