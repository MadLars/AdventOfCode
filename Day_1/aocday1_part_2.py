import math
import csv

def calc(n: int) -> int:
    return max(n // 3 - 2, 0)

sumall = 0

with open("D:\\aoc_day1_input.csv", "r") as f:
     reader = csv.reader(f)
     for row in reader:  
         y=''.join(map(str, row))     
         z=int(y)
         while z > 0:
             z = calc(z)
             sumall += z

print(sumall)
