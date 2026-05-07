#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    # Handle the empty case
    if not intervals:
        return []

    # Step 1: Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Initialize merged list with the first interval
    merged = [intervals[0]]

    # Step 3: Iterate through the remaining intervals
    for current in intervals[1:]:
        last_merged_start, last_merged_end = merged[-1]
        current_start, current_end = current

        # Check for overlap: current start is <= last merged end
        if current_start <= last_merged_end:
            # Merge by updating the end time to the maximum value
            merged[-1][1] = max(last_merged_end, current_end)
        else:
            # No overlap, add the current interval as a new entry
            merged.append(current)

    return merged

if __name__ == '__main__':
