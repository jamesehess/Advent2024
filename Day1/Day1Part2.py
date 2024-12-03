# -----------------------
#   Advent of Code 2024
#   Day 1 Part 2
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

scores = []

for firstvalue in firstlist:
    count = 0
    for secondvalue in secondlist:
        if firstvalue == secondvalue:
            count += 1
    scores.append(firstvalue*count)

print(sum(scores))