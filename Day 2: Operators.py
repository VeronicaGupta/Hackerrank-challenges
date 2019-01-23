#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    #a= meal_cost * (tip_percent/100)
    #b= meal_cost * (tax_percent/100)
    #print((tip_percent + tax_percent) / 100.0)
    #print(meal_cost * (1 + (tip_percent + tax_percent) / 100.0))
    #print(a+b)
    #print(meal_cost + a + b)
    #print(math.floor(meal_cost + a + b ))
    cost = meal_cost * (1 + (tip_percent + tax_percent) / 100.0)

    # cast the result of the rounding operation to an int and save it as totalCost
    #totalCost = math.floor(cost)
    totalCot = round(cost)
    # Print your result
    #print(totalCost)
    print(totalCot)



if __name__ == '__main__':

    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
