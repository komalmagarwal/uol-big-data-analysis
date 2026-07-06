# reducer_q1_mse.py
#!/usr/bin/env python3
import sys

total_error = 0.0
count = 0

for line in sys.stdin:
    try:
        _, values = line.strip().split("\t")
        sq_error, n = values.split(",")
        total_error += float(sq_error)
        count += int(n)
    except:
        continue

mse = total_error / count
print(f"simple_regression_mse\t{mse:.6f}")
print(f"count\t{count}")