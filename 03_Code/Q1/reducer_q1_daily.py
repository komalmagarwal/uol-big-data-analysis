#!/usr/bin/env python3
import sys
import math

current_date = None
count = 0
sum_temp = 0.0
sum_temp_sq = 0.0
min_temp = None
max_temp = None
sum_wind = 0.0
max_wind = None

def emit(date):
    mean_temp = sum_temp / count
    variance = (sum_temp_sq / count) - (mean_temp ** 2)
    std_temp = math.sqrt(max(variance, 0))
    mean_wind = sum_wind / count

    print(f"{date}\t{min_temp:.2f},{max_temp:.2f},{mean_temp:.2f},{std_temp:.2f},{mean_wind:.2f},{max_wind:.2f}")

for line in sys.stdin:
    try:
        date, values = line.strip().split("\t")
        dry_temp, wind_speed = map(float, values.split(","))
    except:
        continue

    if current_date is None:
        current_date = date

    if date != current_date:
        emit(current_date)
        current_date = date
        count = 0
        sum_temp = 0.0
        sum_temp_sq = 0.0
        min_temp = None
        max_temp = None
        sum_wind = 0.0
        max_wind = None

    count += 1
    sum_temp += dry_temp
    sum_temp_sq += dry_temp ** 2
    min_temp = dry_temp if min_temp is None else min(min_temp, dry_temp)
    max_temp = dry_temp if max_temp is None else max(max_temp, dry_temp)
    sum_wind += wind_speed
    max_wind = wind_speed if max_wind is None else max(max_wind, wind_speed)

if current_date is not None and count > 0:
    emit(current_date)