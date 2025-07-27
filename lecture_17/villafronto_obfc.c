#include <stdio.h>

const int A = 20;
const long int T =  20 * 1000 * 1000;
const int B = 12;
const int W = B * 2;
const int D = 1000;

int cnt_no_w() {
    int d = 0;
    long int pa = 0;
    int m = 0;
    while (pa < T) {
        d += 1;
        m += D; 
        pa += m * B;
    }
    return d;
}


int cnt_w() {
    int d = 0;
    long int pa = 0;
    int m = 0;
    while (pa < T) {
        d += 1;
        if (d <= 3) {
            m += D;
        }
        pa += m * W;
    }
    return d;
}


int main() {
    int d_no_w = cnt_no_w();
    int d_w = cnt_w();

    printf("Days without whip: %d, days with whip: %d\n", d_no_w, d_w);
    if (d_no_w == d_w) {
        printf("the same\n");
    }
    if (d_no_w < d_w) {
        printf("without whip faster\n");
    }
    if (d_no_w > d_w) {
        printf("with whip faster\n");
    }
    return 0;
}
