#!/usr/bin/env python3

import random

x = random.randint(0, 1)

def flip(int: x) -> str:
    if x == 1:
        return "Heads"
    else:
        return "Tails"

print(flip(x))
