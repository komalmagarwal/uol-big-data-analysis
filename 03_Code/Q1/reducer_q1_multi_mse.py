#!/usr/bin/env python3
import sys

total_error = 0.0
count = 0

for line in sys.stdin:
    try:
        _, values = line.strip().split("\t")
        err, n = values.split(",")
        total_error += float(err)
        count += int(n)
    except:
        continue

print(f"two_variable_regression_mse\t{total_error / count:.6f}")
print(f"count\t{count}")