from IPython.display import clear_output
import time
myTodo = []

def printview():
    for item in myTodo:
        print(item)

def addview(item): 
    myTodo.append(item)


print("To Do List Manager")

while True:
    action = input("Do you want to view, add, edit or delete your to do list?")

    if action == "view":
        printview()

    elif action == "add":
        item = input("add to do >")
        for x in myTodo:
            if item == x:
                print("Oops you already added this")
            else:
                addview(item)

        continue

    elif action == "edit":
        editaction = ("Do you want to remove or edit an item?")
        printview()
        if editaction == "remove":
            printview()
            item = input("item to remove >")
            myTodo.remove(item)
            printview()
            time.sleep(1)
        elif editaction == "edit":
            printview()
            item = input("item to edit >")
            itemtoedit = input("edit as >")
            myTodo.remove(item)
            addview(itemtoedit)
        clear_output(wait=True)

        continue

    elif action == "delete":
        myTodo.clear()

    else:
        break

printview()
print("Program Ends")