#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    if not row or row[0] == "Wban Number":
        continue

    try:
        x1 = float(row[9].strip())    # Dew Point Temp
        x2 = float(row[11].strip())   # Relative Humidity
        y = float(row[8].strip())     # Dry Bulb Temp

        print(f"multi\t{x1},{x2},{y},{x1*x1},{x2*x2},{x1*x2},{x1*y},{x2*y},1")
    except:
        continue