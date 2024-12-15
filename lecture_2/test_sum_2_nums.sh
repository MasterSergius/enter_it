#!/bin/bash

# test 1
actual=$(./sum_2_nums 3 5)
if [[ $actual -ne 8 ]]; then
  echo "test 1 failed"
  exit 1
fi

# test 2
actual=$(./sum_2_nums 100 200)
if [[ $actual -ne 300 ]]; then
  echo "test 2 failed"
  exit 1
fi

# test 3
actual=$(./sum_2_nums 30000 30000)
if [[ $actual -ne 60000 ]]; then
  echo "test 3 failed"
  exit 1
fi

echo "all tests passed"
