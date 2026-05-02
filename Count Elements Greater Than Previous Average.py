#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    if len(responseTimes) < 2:   
    
        return 0
  
    count = 0
    running_sum= 0
  
    for i in range(len(responseTimes)) :
    
        if i > 0:
            average = running_sum/i
        
            if responseTimes[i] > average:
                count+=1
            
        running_sum+=responseTimes[i]
    return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
