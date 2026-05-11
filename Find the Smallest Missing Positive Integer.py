#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def findSmallestMissingPositive(orderNumbers):
    # length of the arrays is found to know the index value and index value is important to arrange the array in proper order to find the missing value. 
    n = len(orderNumbers)
    # Method: Cyclic Sort / In-place swap
    for i in range(n):
        # While the current number is in the valid range (1 to n)
        # AND it is not at its correct index (number x should be at index x-1)
        # AND the target index doesn't already have the correct number (prevents infinite loop with duplicates)
        #as we are finding the number in range to 1 to n so the line1 is about the same thing and also about finding all the different means the number in array should be not same 
        while 1 <= orderNumbers[i] <= n and orderNumbers[i] != orderNumbers[orderNumbers[i] - 1]:
            # Swap the number to its "home" index
            # and as it goes on, now we found the number and now, ot should be at it place means it should at correct index so the next line is for that 
            target_idx = orderNumbers[i] - 1
            #this statement is precaution for  a SyntaxError being causing. is Checks for Same Object
            orderNumbers[i], orderNumbers[target_idx] = orderNumbers[target_idx], orderNumbers[i]

    # Method: Verification Scan
    # Look for the first index where the 'home' occupant is wrong
    # and this below is method/loop for finding if their is any missing value in array and if not it will return the value which is next value after the whole array 
    for i in range(n):
        if orderNumbers[i] != i + 1:
            return i + 1
            
    # If all numbers 1 to n are present, the smallest missing is n + 1
    return n + 1
    

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
