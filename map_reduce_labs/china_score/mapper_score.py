#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    parts = line.split("***")


    score = float(parts[0])
    city = parts[1]

    print(f"{city}\t{score}")
