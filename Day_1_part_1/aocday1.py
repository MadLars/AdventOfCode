import math
import csv

sumall = 0
# while True:
#     mass = input("Enter the mass of the module: ")
#     sum = math.floor(int(mass) / 3)-2
#     print("The fuel required for this module is: ", sum)
#     sumall += sum
#     print("The fuel required for all modules so far is: ", sumall)
#     YesorNo = input("Do you want to input another module? Y or N : ")
#     if YesorNo == "N":
#          break
#     elif YesorNo == "n":
#          break

with open("C:\\Users\\gollu\\Desktop\\aoc_day1_input.csv", "r") as f:
     reader = csv.reader(f)
     for row in reader:
          
          y=''.join(map(str, row))
          z=int(y)          
          #print("this is z  ", z)
          sum = math.floor((z) / 3)-2
          sumall += sum
          #print("this is sumall inner  ", sumall)

print(sumall)