if __name__ == '__main__':
    print("Hello, World!")

#2

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2!=0:
    print("Weird")
elif n%2==0 and n >= 2 and n <= 5:
    print("Not Weird")
elif n%2==0 and n >= 6 and n <= 20:
    print("Weird")
elif n%2==0 and n > 20:
    print("Not Weird")

#3

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a+b)
print(a-b)
print(a*b)

#4

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)


#5
for x in range(n):
    print(x*x)

#6
for x in range(n):
    print(x+1, end="")

#7

def print_full_name(first, last):
    print("Hello "+first+" "+last+"! You just delved into python.")
    # Write your code here

if __name__ == '__main__':


#8 strings are immutable

def swap_case(s):
    res = ""
    for x in s:
        if x.islower():
            res += x.upper()
        else:
            res += x.lower()
    return res


#9
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    scores = list(set(arr))   # remove duplicates
    scores.sort()

    print(scores[-2])

#10

import textwrap

def wrap(string, max_width):
    res = ""
    cnt = 0
    out = ""
    
    for x in range(len(string)):
        cnt += 1
        res += string[x]
        
        if cnt == max_width:
            out += res + "\n"
            res = ""
            cnt = 0
    
    if cnt > 0:
        out += res
        
    return out

