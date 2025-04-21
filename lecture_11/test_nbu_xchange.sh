#!/usr/bin/env bash
# this will pass only if amount is the same as on nbu website for given date
amount=$(python3 nbu_xchange.py EUR USD 1000)
echo $amount
if [ $amount == "1154.35" ]; then
  echo "test passed"
else
  echo "test failed"
fi
