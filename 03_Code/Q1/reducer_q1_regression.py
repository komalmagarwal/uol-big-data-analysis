#!/usr/bin/env python3
import sys

sum_x = 0.0
sum_y = 0.0
sum_x2 = 0.0
sum_xy = 0.0
n = 0

for line in sys.stdin:
    try:
        key, values = line.strip().split("\t")
        x, y, x2, xy, count = values.split(",")

        sum_x += float(x)
        sum_y += float(y)
        sum_x2 += float(x2)
        sum_xy += float(xy)
        n += int(count)

    except:
        continue

denominator = (n * sum_x2) - (sum_x ** 2)

if denominator == 0:
    print("Error: denominator is zero")
else:
    slope = ((n * sum_xy) - (sum_x * sum_y)) / denominator
    intercept = (sum_y - (slope * sum_x)) / n

    print(f"model\tpredict_dry_bulb_temp = {slope:.6f} * dew_point_temp + {intercept:.6f}")
    print(f"slope\t{slope:.6f}")
    print(f"intercept\t{intercept:.6f}")
    print(f"count\t{n}")