#!/usr/bin/env python3
import sys
import math

current_key = None
n = 0
sum_x = 0.0
sum_y = 0.0
sum_x2 = 0.0
sum_y2 = 0.0
sum_xy = 0.0

def emit_result(key):
    mean_x = sum_x / n
    mean_y = sum_y / n

    covariance = (sum_xy / n) - (mean_x * mean_y)

    var_x = (sum_x2 / n) - (mean_x ** 2)
    var_y = (sum_y2 / n) - (mean_y ** 2)

    if var_x <= 0 or var_y <= 0:
        correlation = 0.0
    else:
        correlation = covariance / math.sqrt(var_x * var_y)

    print(f"{key}\tcount={n}, covariance={covariance:.4f}, correlation={correlation:.4f}")

for line in sys.stdin:
    try:
        key, values = line.strip().split("\t")
        x, y = map(float, values.split(","))
    except:
        continue

    if current_key is None:
        current_key = key

    if key != current_key:
        emit_result(current_key)

        current_key = key
        n = 0
        sum_x = 0.0
        sum_y = 0.0
        sum_x2 = 0.0
        sum_y2 = 0.0
        sum_xy = 0.0

    n += 1
    sum_x += x
    sum_y += y
    sum_x2 += x * x
    sum_y2 += y * y
    sum_xy += x * y

if current_key is not None and n > 0:
    emit_result(current_key)