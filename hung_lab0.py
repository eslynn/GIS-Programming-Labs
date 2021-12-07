# Steffi Hung
# GIS: Programming and Automation
# Fall 2021
# Assignment: Lab 0

#

# Lab 0: Part I
# Create lists
ls_hypFile = ["roads", "cities", "counties", "states"]
ls_hypFileXt = []

# Create 'for loop' to edit lists
for i in ls_hypFile:
    ls_hypFileXt.append(i + ".txt")
    
# print list to verify code works
print(ls_hypFileXt)

#

#Lab 0: Part II
#import pi and sets variables
from math import pi
pwr = 0
piSq = pi ** pwr
piBox = []

#creates while loop
while piSq < 10000:
    piSq = pi ** pwr
    if piSq < 10000:
        piBox.append(piSq)
        pwr = pwr + 1
    else:
        break
    
#prints list to check code
print (piBox)