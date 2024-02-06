#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

# if n is odd  
if n % 2 != 0:
    print("Weird")
# if n is even & in range of 2 to 5
elif n % 2 == 0 and n in range(2, 6):
    print("Not Weird")
# if n is even & in range of 6 to 20
elif n % 2 == 0 and n in range(6, 21):
    print("Weird")
# if n is even and > 20
elif n % 2 == 0 and n > 20:
    print("Not Weird")
