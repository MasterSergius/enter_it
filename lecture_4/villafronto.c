/*
Total area of grass - 20 sqr km
Base productivity - 12 sqr m
Productivity with whip - Base productivity * 2 sqr m
Delivery count - 1000 monkeys
Delivery time - 2 days

What if more efficent - work with whip or without whip?

area of painted grass = 0
Day 1: area of painted grass += delivery count * base productivity
Day 2: area of painted grass += delivery count * 2 * base productivity
Day 3: area of painted grass += delivery count * 3 * base productivity
...
Day X: area of painted grass += delivery count * x * base productivity
until area of painted grass >= Total area of grass

Algorithm
1. Count days with whip and without whip
    1.1. Count day without whip
        1.1.1. start painted grass = 0
        1.1.2. monkeys = 0, days 0
        1.1.3. monkeys += delivery count, days += 1
        1.1.4. painted grass += monkeys * base productivity
        1.1.5. if painted grass < total area of grass then goto 1.1.3
        1.1.6. return days
    1.2. Count day with whip
        1.1.1. start painted grass = 0
        1.1.2. monkeys = 0, days 0
        1.1.3. monkeys += delivery count, days += 1
        1.1.4. if days > 3 then monkeys -= delivery_count
        1.1.5. painted grass += monkeys * base productivity
        1.1.6. if painted grass < total area of grass then goto 1.1.3
        1.1.7. return days
2. Compare days and print result
*/

#include <stdio.h>

const int total_area_sqr_km = 20;
const long int total_area_sqr_m = 20 * 1000 * 1000;
const int base_productivity_sqr_m = 12;
const int whip_productivity_sqr_m = base_productivity_sqr_m * 2;
const int delivery_count_monkeys = 1000;


int count_days_without_whip() {
    int days = 0;
    long int painted_area = 0;
    int monkeys = 0;
    while (painted_area < total_area_sqr_m) {
        days += 1;
        monkeys += delivery_count_monkeys;
        painted_area += monkeys * base_productivity_sqr_m;
    }
    return days;
}


int count_days_with_whip() {
    int days = 0;
    long int painted_area = 0;
    int monkeys = 0;
    while (painted_area < total_area_sqr_m) {
        days += 1;
        if (days <= 3) {
            monkeys += delivery_count_monkeys;
        }
        painted_area += monkeys * whip_productivity_sqr_m;
    }
    return days;
}


int main() {
    int days_without_whip = count_days_without_whip();
    int days_with_whip = count_days_with_whip();

    printf("Days without whip: %d, days with whip: %d\n", days_without_whip, days_with_whip);
    if (days_without_whip == days_with_whip) {
        printf("the same\n");
    }
    if (days_without_whip < days_with_whip) {
        printf("without whip faster\n");
    }
    if (days_without_whip > days_with_whip) {
        printf("with whip faster\n");
    }
    return 0;
}
