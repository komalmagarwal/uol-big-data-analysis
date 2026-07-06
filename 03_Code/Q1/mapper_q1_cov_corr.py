#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    if not row or row[0] == "Wban Number":
        continue

    try:
        dry = float(row[8].strip())
        dew = float(row[9].strip())
        humidity = float(row[11].strip())

        print(f"dew_point\t{dry},{dew}")
        print(f"humidity\t{dry},{humidity}")
    except:
        continue