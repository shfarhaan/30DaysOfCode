#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    current_consecutive_1s = 0
    maximum_consecutive_1s = 0
    
    while n > 0:
        remainder = n % 2
        if remainder == 1:
            current_consecutive_1s += 1
            if current_consecutive_1s > maximum_consecutive_1s:
                maximum_consecutive_1s = current_consecutive_1s
        else:
            current_consecutive_1s = 0
        n = n // 2
    print(maximum_consecutive_1s)
