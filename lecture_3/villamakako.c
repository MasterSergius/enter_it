/*
10 square km - whole grass
12 square m - productivity of work of 1 monkey
if major gives bananas, then productivity of work - 18 square m

quantity of monkeys?

Algorithm

1. Translate square kilometers to square meters
2. If major gives bananas productivity = 18, else = 12
2. Divide whole square of grass by monkey productivity of work
3. Ceil result
*/

#include <stdio.h>
#include <math.h>
#include <stdbool.h>


int main() {
  const int all_grass_km = 10;
  const int productivity_without_bananas = 12;
  const int productivity_with_bananas = 18;
  bool bananas = true;
  int productivity_m;
  // short form, if we have only one operation, we don't need brackets - {}
  if (bananas) productivity_m = productivity_with_bananas; else productivity_m = productivity_without_bananas;
  // 1 km - 1000 m, 1 square km = 1000 m * 1000 m = 1000000 square m
  float monkeys = all_grass_km * 1000 * 1000 / productivity_m;
  long int monkeys_int = (int)ceil(monkeys);
  printf("%ld\n", monkeys_int);
  return 0;
}
