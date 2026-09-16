import csv
import os
from datetime import date

print("Welcome to my Family Expense Tracker!")

total_budget = 0
total_family_spent = 0

today = date.today()

while True:
    category = input("\nEnter the expense category, or type 'done' to finish: ")

    if category.lower() == "done":
        break

    budget = float(input("\nEnter the budget for this category: ₹"))

    total_spent = 0

    while True:
        amount = input("\nEnter an expense amount, or type 'done' to finish: ")

        if amount.lower() == "done":
            break

        amount = float(amount)
        total_spent = total_spent + amount

        file_exists = os.path.exists("expenses.csv")

        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Date", "Category", "Amount"])

            writer.writerow([today, category, amount])

    remaining = budget - total_spent

    total_budget = total_budget + budget
    total_family_spent = total_family_spent + total_spent

    print("\nEXPENSE SUMMARY:")
    print("Category:", category)
    print("Budget: ₹", budget)
    print("Total spent: ₹", total_spent)
    print("Money remaining: ₹", remaining)


total_remaining = total_budget - total_family_spent

print("\nOVERALL SUMMARY:")
print("Total budget: ₹", total_budget)
print("Total spent: ₹", total_family_spent)
print("Total remaining: ₹", total_remaining)


print("\nMONTHLY SPENDING SUMMARY:")

month = input("Enter the month you want to check (YYYY-MM): ")

monthly_total = 0

with open("expenses.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Date"].startswith(month):
            if row["Amount"].lower() != "done":
                monthly_total = monthly_total + float(row["Amount"])

print("Total spent in", month, ": ₹", monthly_total)

print("\nThank you for using the Family Expense Tracker!")