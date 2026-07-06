#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    if not row or row[0] == "Wban Number":
        continue

    try:
        x = float(row[9].strip())   # Dew Point Temp
        y = float(row[8].strip())   # Dry Bulb Temp

        print(f"regression\t{x},{y},{x*x},{x*y},1")
    except:
        continue
    