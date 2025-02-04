"""Ball"""
def main(high,count) :
    """High"""
    while high >= 0.01 :
        high = high * (3 / 5)
        count += 1
    count -= 1
    print(count)
main(float(input()),0)
