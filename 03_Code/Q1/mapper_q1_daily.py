#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    if not row or row[0] == "Wban Number":
        continue

    try:
        date = row[1].strip()
        dry_temp = float(row[8].strip())
        wind_speed = float(row[12].strip())
        print(f"{date}\t{dry_temp},{wind_speed}")
    except:
        continue
    