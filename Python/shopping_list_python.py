""" lists
Simple program that allows management of a list by a user
NB lists start at index number of 0 and so a list of four items goes from [0] to [3]"""
import random
import fileinput
import atexit

items =[]
for line in fileinput.input("shopping_list.txt"):
    items.append(line.strip())
def manage_list():
    choice = input("Enter A to add an item, D to delete an item, S to save the shopping-list ")
    if choice.upper() == "A":
        newgreeting = input("Enter the new item ")
        items.append(newgreeting)
    if choice.upper() == "D":
        decision = input("Enter I to enter the index number or M to enter the item name you want to delete")
        if decision.upper() == "I":
            i_to_delete = int(input("Enter the index number of the item you want to delete"))
            items.pop(i_to_delete-1)
        if decision.upper() == "M":
            m_to_delete = input("Enter the item name you would like to delete")
            for p, i in enumerate(items):
                if i.upper() == m_to_delete.upper():
                    items.pop(p)
                    print("Successfully deleted!")
    if choice.upper() == "S":
        file = open("shopping_list.txt", "w")
        for i in range(0, len(items)):
            file.write(str(items[i]) + "\n")
        file.close()
        print ("Saved!")
def bye():
    file = open("shopping_list.txt", "w")
    for i in range(0, len(items)):
        file.write(str(items[i]) + "\n")
    file.close()
    print ("Saved!")
"""def random_entry():
    i =random.randint(0,len(items)-1)
    print(items[i])"""

print("List: ", items)

while 1==1:
    choice = input("Enter M for manage list, V for view list ")
    if choice.upper() == "M":
        manage_list()
#    if choice.upper() == "R":
#       random_entry()
    if choice.upper() == "V":
        print(items)

atexit.register(bye)
""" Tasks:
1) Try the program as it is
2) Create the if block and define the function for the view list option.
TEST THIS CHANGE
3) Add an option to allow the user to enter the greeting number to display
TEST IT AGAIN
4) For the Brave only.......Change the delete option so that the user enters the greeting
   to delete rather than its index number"""
#if finished:
#    http://docs.python.org/3.3/tutorial/introduction.html OR continue Python for Kids#
