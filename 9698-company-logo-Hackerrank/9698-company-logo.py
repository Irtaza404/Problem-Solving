#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s=Counter(sorted(input(),key=str.lower))
    for c,num in sorted(s.items(),key=lambda x:x[1],reverse=True)[:3]:
        print(f"{c} {num}")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna