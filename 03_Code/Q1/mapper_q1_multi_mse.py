#!/usr/bin/env python3
import sys
import csv

B0 = 46.079243
B1 = 1.034409
B2 = -0.522485

reader = csv.reader(sys.stdin)

for row in reader:
    if not row or row[0] == "Wban Number":
        continue
    try:
        x1 = float(row[9].strip())
        x2 = float(row[11].strip())
        y = float(row[8].strip())

        y_hat = B0 + B1 * x1 + B2 * x2
        sq_error = (y - y_hat) ** 2
        print(f"multi_mse\t{sq_error},1")
    except:
        continue