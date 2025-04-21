#!/usr/bin/env bash

python3 quadratic.py 1 5 6
echo "correct solution: -3, -2"
python3 quadratic.py 1 -5 6
echo "correct solution: 2, 3"
python3 quadratic.py 1 2 3
echo "correct solution: no solution"
