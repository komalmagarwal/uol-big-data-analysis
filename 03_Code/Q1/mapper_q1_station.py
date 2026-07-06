#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:

    if not row or row[0] == "Wban Number":
        continue

    try:
        station = row[0].strip()

        dry = float(row[8].strip())
        wind = float(row[12].strip())

        print(f"{station}\t{dry},{wind}")

    except:
        continue