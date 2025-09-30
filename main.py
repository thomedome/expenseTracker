import csv # Rows --> [Category, Cost, Date]
from time import sleep as wait
import datetime as dt
import os

categories = ["entertainment", "bills", "food", "transport", "housing", "health", "shopping", "education", "travel", "finance", "gifts", "other"] # Categories of expendatures

class expenseObject(): # Used to easily manage expenses
    def __init__(self, category, date, amount):
        self.category = category
        self.date = date
        self.amount = amount
    
    def __str__(self):
        return f"{self.category}, {self.amount}, {self.date}"

def cls():
    os.system("cls")

# def openReadCSV():
#     with open("expenses.csv", mode="r") as readFile:
#         return readFile

def writeToCSV(obj):
    csv.writer()

def chooseCategory():
    cls()
    print("Please select a category for your new expendature:")

    for cat in categories: # List Categories
        print(" -",cat.capitalize(), end="\n")

    chosen = str(input("Type your chosen category: \n")) # Get Category

    if chosen.lower() in categories:
        # Continue
        return chosen.lower()
    else:
        # Retry
        print("This is not a category - please try again.")
        wait(2)
        chooseCategory()

def addAmount():    
    cls()
    print("Please type the amount spent:")

    amount = int(input("")) # figure out how to validate as int later without errors. i am as some say, stumped.  
    return amount
         
def addExpense():
    cat = chooseCategory()
    amount = addAmount()
    dateFull = dt.datetime.now()
    date = dateFull.strftime("%d/%m/%Y")
    newExp = expenseObject(cat, date, amount)

    with open("expenses.csv", mode="a", newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow([newExp.category, newExp.amount, newExp.date])
        writeFile.close()

def getTotalSpend():
    amount = 0
    with open("expenses.csv", mode="r") as readFile:
        reader = csv.reader(readFile)
        next(reader, None) # Skip header row

        for row in reader:
            amount += int(row[1]) # Row 2 - Cost
 
    print(amount)

getTotalSpend()
# addExpense()