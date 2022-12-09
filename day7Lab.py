# Program to work with lists
#
# Written by Ben Wheeler
# Culver-Stockton College    12/8/2018
#
# Initialize list
mylist = [ ]
# Set up loop to put menu on screen
num = 1
while num != 0 :
  print(" ")
  print(" ")
  print("            Menu  ")
  print ("0 - Quit")
  print ("1 - Add item to list")
  print ("2 - Pop item off list and print it")
  print ("3 - Print list")
  print ("4 - Sort list")
  print ("5 - Reverse list")
  snum = input("Enter choice from menu ")
  num = int(snum)
  if num == 0:
    print("Program Terminated")
  if num == 1:
    x = int(input("Enter integer for list "))
    mylist.append(x)
  if num == 2:
    x = mylist.pop()
    print("Value popped: " + str(x))
  if num == 3:
    print(mylist)
  if num == 4:
    mylist.sort()
  if num == 5:
    mylist.reverse()
  if num<0 or num>5:
    print("Invalid entry, try again")
  print (" ")
