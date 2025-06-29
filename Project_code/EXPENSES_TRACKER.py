import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

FILE = "expenses.json"
CATEGORIES = ["Food", "Transport", "Stationary", "Bills", "Health", "Others"]

# Load data
def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save data
def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add new expense
def add_expenses():
    print("\nADD NEW EXPENSE:")
    date_str = input("Enter date (yyyy-mm-dd) or leave blank for today: ")
    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print(" PLEASE ENTER A VALID DATE (yyyy-mm-dd)!")
        return

    print("SELECT A CATEGORY:")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}. {cat}")
    try:
        cat_choice = int(input("Enter category number: "))
        category = CATEGORIES[cat_choice - 1]
    except:
        print(" INVALID CATEGORY CHOICE!")
        return

    try:
        amount = float(input("Enter amount: ₹ "))
    except:
        print(" INVALID AMOUNT!")
        return

    expense = {
        'date': date_str,
        'category': category,
        'amount': amount
    }

    data = load()
    data.append(expense)
    save(data)
    print(" Expense saved successfully!")

# Show monthly report
def show():
    data = load()
    if not data:
        print("No expenses found.")
        return

    month = input("Enter month (YYYY-MM): ")
    monthly_totals = {}

    for exp in data:
        if exp['date'].startswith(month):
            cat = exp['category']
            monthly_totals[cat] = monthly_totals.get(cat, 0) + exp['amount']

    if not monthly_totals:
        print("No expenses found for this month.")
        return

    print("\nMonthly Report:")
    for cat, total in monthly_totals.items():
        print(f"{cat}: ₹{total:.2f}")

    draw_charts(monthly_totals, month)

# Draw charts
def draw_charts(monthly_totals, month):
    categories = list(monthly_totals.keys())
    amounts = list(monthly_totals.values())

    # Pie Chart
    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title(f"Expenses Pie Chart - {month}")
    plt.show()

    # Bar Chart
    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color='skyblue')
    plt.title(f"Expenses Bar Chart - {month}")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.show()

# Main Menu
def main_app():
    while True:
        print("\n Expense Tracker CLI")
        print("1. Add Expense")
        print("2. Show Monthly Report")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expenses()
        elif choice == '2':
            show()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main_app()
