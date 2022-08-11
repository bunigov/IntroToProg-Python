# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1/1/2020,Created started script
# BorisU,8/8/2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

from random import randint, randrange

#  ---- RUN ONCE  ------  #
# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# File to List

objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")  # Returns a list!
    dicRow = {"Id": lstRow[0], "Task": lstRow[1], "Priority": lstRow[2].strip()}
    lstTable.append(dicRow)
print("Items successfully loaded from " + strFile)
#print(lstTable)
# Showing the current contents of the list  (better to put this into a function since reusing)
print("File contents loaded..")  # if no current items may want to present another message
print("Id" + " | " + "Task" + " | " + "Priority")  # remove hardcoding later to use the dynamic keys
for row in lstTable:
    print(row["Id"] + "," + row["Task"] + "," + row["Priority"])
objFile.close()

#  ---- RUN UNTIL STOPPED  ------  #
while (True):
    # -- Input/Output -- #
     # Step 2 - Display a menu of choices to the user
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    # Print column headers
    # Loop through each row printing out the values by the key
    if (strChoice.strip() == '1'):
        print("Listing current items..")  #if no current items may want to present another message
        print("Id" + " | " + "Task" + " | " + "Priority")   #remove hardcoding later to use the dynamic keys
        for row in lstTable:
            print(row["Id"] + "," + row["Task"] + "," + row["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    # Get user input for task name and priority,
    # Create a row to add as a dictionary row,
    # Append the dictionary row to the master table (stored as a list)
    # Print out information to the user
    elif (strChoice.strip() == '2'):
        strId = str(randint(100000, 999999))  #random 6 digit number  (needed for removing items in the future)
        strTask = input("Please specify a \'Task\': ")
        strPriority = input("Please specify a \'Priority\': ")
        dicRow = {"Id": strId, "Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Task and Priority added to the list...")
        #print(lstTable)

        # Showing the current contents of the list  (better to put this into a function since reusing)
        print("List current items (post add)..")  # if no current items may want to present another message
        print("Id" + " | " + "Task" + " | " + "Priority")  # remove hardcoding later to use the dynamic keys
        for row in lstTable:
            print(row["Id"] + "," + row["Task"] + "," + row["Priority"])
        objFile.close()
        continue

    # Step 5 - Remove a new item from the list/Table
    # Show current list
    # Ask for id to be removed
    # Loop through the list
    # For id to be removed, generate a dictionary row to be removed
    # Use remove command to remove that dictionary row
    # Inform the user / shpw updated list
    elif (strChoice.strip() == '3'):
        # Showing the current contents of the list  (better to put this into a function since reusing)
        print("Listing current items pre removal..")  # if no current items may want to present another message
        print("Id" + " | " + "Task" + " | " + "Priority")  # remove hardcoding later to use the dynamic keys
        for row in lstTable:
            print(row["Id"] + "," + row["Task"] + "," + row["Priority"])

        print()
        strIdToDelete = input("Please specify the Id of the item to Delete: ")
        #lstTable.remove(dicRow)
        for row in lstTable:
            if row["Id"] == strIdToDelete:
                dicRowToDelete = {"Id": strIdToDelete, "Task": row["Task"], "Priority": row["Priority"]}
                lstTable.remove(dicRowToDelete)
                print()
                print(str(dicRowToDelete) + "  has been Removed..." + "\n")

        # Showing the current contents of the list  (better to put this into a function since reusing)
        print("Listing current items post removal..")  # if no current items may want to present another message
        print("Id" + " | " + "Task" + " | " + "Priority")  # remove hardcoding later to use the dynamic keys
        for row in lstTable:
            print(row["Id"] + "," + row["Task"] + "," + row["Priority"])
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    # Open the file connection
    # Loop through each row writing to the file the two elements using the key
    # Close the connection
    # Inform the user
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "a") # append does create the file if not existing
        for row in lstTable:
            objFile.write(row["Id"] + "," + row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("Data Saved to File")
        continue

    # Step 7 - Exit program
    # Notify the user that the program has exit
    # Break out of the while loop
    elif (strChoice.strip() == '5'):
        print("Program exited")
        break  # and Exit the program
