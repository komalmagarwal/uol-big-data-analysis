#!/usr/bin/env python3

import sys
import math

current_station = None

count = 0

sum_dry = 0.0
sum_dry_sq = 0.0

sum_wind = 0.0
sum_wind_sq = 0.0

min_dry = None
max_dry = None

min_wind = None
max_wind = None


def emit():

    dry_mean = sum_dry / count
    wind_mean = sum_wind / count

    dry_var = (sum_dry_sq / count) - (dry_mean ** 2)
    wind_var = (sum_wind_sq / count) - (wind_mean ** 2)

    dry_std = math.sqrt(max(dry_var, 0))
    wind_std = math.sqrt(max(wind_var, 0))

    print(
        f"{current_station}\t"
        f"{count},"
        f"{dry_mean:.2f},"
        f"{dry_var:.2f},"
        f"{dry_std:.2f},"
        f"{min_dry:.2f},"
        f"{max_dry:.2f},"
        f"{wind_mean:.2f},"
        f"{wind_var:.2f},"
        f"{wind_std:.2f},"
        f"{min_wind:.2f},"
        f"{max_wind:.2f}"
    )


for line in sys.stdin:

    try:
        station, values = line.strip().split("\t")
        dry, wind = map(float, values.split(","))
    except:
        continue

    if current_station is None:
        current_station = station

    if station != current_station:

        emit()

        current_station = station

        count = 0

        sum_dry = 0.0
        sum_dry_sq = 0.0

        sum_wind = 0.0
        sum_wind_sq = 0.0

        min_dry = None
        max_dry = None

        min_wind = None
        max_wind = None

    count += 1

    sum_dry += dry
    sum_dry_sq += dry * dry

    sum_wind += wind
    sum_wind_sq += wind * wind

    min_dry = dry if min_dry is None else min(min_dry, dry)
    max_dry = dry if max_dry is None else max(max_dry, dry)

    min_wind = wind if min_wind is None else min(min_wind, wind)
    max_wind = wind if max_wind is None else max(max_wind, wind)

if current_station is not None:
    emit()