import math
import csv

sumall = 0

with open("D:\\aoc_day1_input.csv", "r") as f:
     reader = csv.reader(f)
     for row in reader:
          
          y=''.join(map(str, row))
          z=int(y)
          sum = math.floor((z) / 3)-2
          sumall += sum

print(sumall)