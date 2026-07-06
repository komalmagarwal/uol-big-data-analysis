#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader, None)

row_id = 0

for row in reader:
    if len(row) < 2:
        continue

    row_id += 1
    ticket1 = row[0].strip()
    ticket2 = row[1].strip()

    if ticket1 and ticket2:
        print(f"{row_id}\t{ticket1}\t{ticket2}")