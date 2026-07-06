# mapper_q1_mse.py
#!/usr/bin/env python3
import sys
import csv

SLOPE = 0.769255
INTERCEPT = 23.330856

reader = csv.reader(sys.stdin)

for row in reader:
    if not row or row[0] == "Wban Number":
        continue

    try:
        x = float(row[9].strip())
        y = float(row[8].strip())
        y_hat = SLOPE * x + INTERCEPT
        sq_error = (y - y_hat) ** 2
        print(f"mse\t{sq_error},1")
    except:
        continue