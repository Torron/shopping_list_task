import random
import fileinput
#import atexit This showed to not work properly

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
"""def bye():
    file = open("shopping_list.txt", "w")
    for i in range(0, len(items)):
        file.write(str(items[i]) + "\n")
    file.close()
    print ("Saved!")""" #Saving on exit didn't work properly
print("List: ", items)

while 1==1:
    choice = input("Enter M for manage list, V for view list ")
    if choice.upper() == "M":
        manage_list()
#    if choice.upper() == "R":
#       random_entry()
    if choice.upper() == "V":
        print(items)

#atexit.register(bye) This didn't seem to work
