import csv
import os

EXPENSES_FILE = "expenses.csv"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        """Loads expenses from the CSV file if it exists."""
        if os.path.exists(EXPENSES_FILE):
            with open(EXPENSES_FILE, mode="r") as file:
                reader = csv.reader(file)
                self.expenses = [row for row in reader]

    def save_expenses(self):
        """Saves expenses to the CSV file."""
        with open(EXPENSES_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.expenses)

    def add_expense(self, date, category, amount, description):
        """Adds a new expense."""
        self.expenses.append([date, category, amount, description])
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        """Displays all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\nDate        | Category   | Amount | Description")
        print("-" * 50)
        for expense in self.expenses:
            print(f"{expense[0]:10} | {expense[1]:10} | ${expense[2]:>6} | {expense[3]}")

    def delete_expense(self, index):
        """Deletes an expense by index."""
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            self.save_expenses()
            print("Expense deleted successfully!")
        else:
            print("Invalid index.")

    def total_expenses(self):
        """Calculates and displays the total amount spent."""
        total = sum(float(expense[2]) for expense in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (Food, Transport, etc.): ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            tracker.add_expense(date, category, amount, description)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.view_expenses()
            index = int(input("Enter the index of expense to delete: "))
            tracker.delete_expense(index)

        elif choice == "4":
            tracker.total_expenses()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
