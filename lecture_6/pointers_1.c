#include <stdio.h>


void add_numbers(int number1, int number2) {
   number1 += number2;
   printf("sum: %d\n", number1);
}


void add_numbers_with_change(int * number1, int number2) {
   *number1 += number2;
   printf("sum: %d\n", *number1);
}


int main() {
  int some_number = 5;
  add_numbers(some_number, 10);
  printf("original number: %d\n", some_number);
  printf("---------------\n");
  add_numbers_with_change(&some_number, 10);
  printf("original number: %d\n", some_number);
  return 0;
}
