#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime, timedelta

# Complete the time_delta function below.
def time_delta(t1, t2):
    # Parse the datetime objects without their respective timezones
    dt1 = datetime.strptime(t1[:-6], "%a %d %b %Y %H:%M:%S")
    dt2 = datetime.strptime(t2[:-6], "%a %d %b %Y %H:%M:%S")
    
    # Parse the timezone offsets
    tz1 = t1[-5:]
    tz2 = t2[-5:]
    
    # Create timedelta objects for the offsets
    tz1_offset = int(tz1[1:3]) * 3600 + int(tz1[3:]) * 60
    tz2_offset = int(tz2[1:3]) * 3600 + int(tz2[3:]) * 60

    if tz1[0] == '-':
        tz1_offset = -tz1_offset
    if tz2[0] == '-':
        tz2_offset = -tz2_offset
    
    # Adjust the datetime objects by their timezone offsets to get UTC times
    dt1_utc = dt1 - timedelta(seconds=tz1_offset)
    dt2_utc = dt2 - timedelta(seconds=tz2_offset)
    
    # Calculate the absolute difference in seconds
    diff_seconds = abs(int((dt1_utc - dt2_utc).total_seconds()))
    return str(diff_seconds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
