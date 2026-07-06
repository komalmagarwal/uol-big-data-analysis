#!/usr/bin/env python3
import sys

n = 0
sx1 = sx2 = sy = 0.0
sx1x1 = sx2x2 = sx1x2 = 0.0
sx1y = sx2y = 0.0

for line in sys.stdin:
    try:
        _, values = line.strip().split("\t")
        x1, x2, y, x1x1, x2x2, x1x2, x1y, x2y, c = values.split(",")

        sx1 += float(x1)
        sx2 += float(x2)
        sy += float(y)
        sx1x1 += float(x1x1)
        sx2x2 += float(x2x2)
        sx1x2 += float(x1x2)
        sx1y += float(x1y)
        sx2y += float(x2y)
        n += int(c)
    except:
        continue

# Normal equations:
# y = b0 + b1*x1 + b2*x2
A = [
    [n, sx1, sx2],
    [sx1, sx1x1, sx1x2],
    [sx2, sx1x2, sx2x2]
]

B = [sy, sx1y, sx2y]

def det3(m):
    return (
        m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1])
        - m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0])
        + m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0])
    )

D = det3(A)

A0 = [[B[0], A[0][1], A[0][2]],
      [B[1], A[1][1], A[1][2]],
      [B[2], A[2][1], A[2][2]]]

A1 = [[A[0][0], B[0], A[0][2]],
      [A[1][0], B[1], A[1][2]],
      [A[2][0], B[2], A[2][2]]]

A2 = [[A[0][0], A[0][1], B[0]],
      [A[1][0], A[1][1], B[1]],
      [A[2][0], A[2][1], B[2]]]

b0 = det3(A0) / D
b1 = det3(A1) / D
b2 = det3(A2) / D

print(f"model\tpredict_dry_bulb_temp = {b0:.6f} + {b1:.6f} * dew_point_temp + {b2:.6f} * relative_humidity")
print(f"intercept\t{b0:.6f}")
print(f"dew_point_coefficient\t{b1:.6f}")
print(f"humidity_coefficient\t{b2:.6f}")
print(f"count\t{n}")