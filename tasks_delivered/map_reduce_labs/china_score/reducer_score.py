#!/usr/bin/env python3
# reducer.py

import sys
import math

city_data = {}

for line in sys.stdin:
    line = line.strip()

    city, score = line.split("\t")
    score = float(score)

    if city not in city_data:
        city_data[city] = []

    city_data[city].append(score)

results = []

for city, scores in city_data.items():

    count = len(scores)
    total = sum(scores)
    mean = total / count

    # variance
    variance = sum((x - mean) ** 2 for x in scores) / count

    # standard deviation
    std_dev = math.sqrt(variance)

    results.append((city, count, mean, std_dev))

# sort by mean descending
results.sort(key=lambda x: x[2], reverse=True)

# print ranked results
rank = 1

for city, count, mean, std_dev in results:
    print(
        f"{rank}\t{city}\tCOUNT={count}\tMEAN={mean:.2f}\tSTD_DEV={std_dev:.2f}"
    )
    rank += 1
