
import os
import json
from datetime import datetime
EXPENSE_FILE = "expenses.json"
def load_expenses():
    """
    """
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    return {"expenses": []}
def save_expenses(expenses):
    """
    Args:
        expenses (dict):
        """
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)
def add_expense(expenses):
    """
    Args:
        expenses (dict): 
    """
    try:
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description of the expense: ").strip()
        category = input("Enter the category (e.g., food, transport, entertainment): ").strip().lower()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        expenses["expenses"].append({
            "amount": amount,
            "description": description,
            "category": category,
            "date": date
        })
        print("Expense added successfully!")
    except ValueError:
        print("Error: Invalid amount. Please enter a numeric value.")
def view_expenses(expenses):
    """
    Args:
        expenses (dict): 
    """
    if not expenses["expenses"]:
        print("No expenses recorded yet.")
        return
    print("\nAll Expenses:")
    for i, expense in enumerate(expenses["expenses"], start=1):
        print(f"{i}. {expense['date']} - ${expense['amount']:.2f} - {expense['category']} - {expense['description']}")
    print()
def view_monthly_summary(expenses):
    """
    Args:
        expenses (dict): 
    """
    month = input("Enter the month (YYYY-MM) to view expenses: ").strip()
    total = 0
    print(f"\nExpenses for {month}:")
    for expense in expenses["expenses"]:
        if expense["date"].startswith(month):
            print(f"- ${expense['amount']:.2f} - {expense['category']} - {expense['description']}")
            total += expense["amount"]
    print(f"\nTotal for {month}: ${total:.2f}")
def view_category_summary(expenses):
    """
    Args:
        expenses (dict): 
    """
    category_totals = {}
    for expense in expenses["expenses"]:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]
    print("\nCategory-wise Summary:")
    for category, total in category_totals.items():
        print(f"- {category}: ${total:.2f}")
def main_menu():
    """
    """
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Summary")
        print("4. View Category-wise Summary")
        print("5. Exit")
        try:
            choice = int(input("Choose an option (1-5): "))
            if choice == 1:
                add_expense(expenses)
                save_expenses(expenses)
            elif choice == 2:
                view_expenses(expenses)
            elif choice == 3:
                view_monthly_summary(expenses)
            elif choice == 4:
                view_category_summary(expenses)
            elif choice == 5:
                print("Exiting the Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Error: Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main_menu()
