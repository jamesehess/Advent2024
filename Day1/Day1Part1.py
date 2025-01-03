# -----------------------
#   Advent of Code 2024
#   Day 1 Part 1
#   Author: James Hess
# -----------------------

lines = []

with open("Day1Input.txt") as file:
    inputlines = file.readlines()
    for inputline in inputlines:
        lines.append(inputline.strip())

firstlist = []
secondlist = []

for line in lines:
    values = line.split("   ")
    firstlist.append(int(values[0]))
    secondlist.append(int(values[1]))

firstlist.sort()
secondlist.sort()

distances = []


for x in range(len(firstlist)):
    distances.append(abs(firstlist[x]-secondlist[x]))

print(sum(distances))