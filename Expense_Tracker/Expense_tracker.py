from datetime import datetime

expense = []

FILE_PATH = r'D:\Sanket\Documents\Coding\Python\python-practice\Expense_Tracker\expenses.txt'


def expense_tracker(code):

    match code:

        case 1:
            print("\n--- Add Expense ---")

            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))

            date = input("Enter date (DD-MM-YYYY): ")
            date = datetime.strptime(date, "%d-%m-%Y")

            category = input("Enter expense category: ")

            new_expense = {
                'name': name,
                'amount': amount,
                'date': date,
                'category': category
            }

            expense.append(new_expense)

            print("Expense added successfully!")

        case 2:
            print("\n--- View Expenses ---")

            if not expense:
                print("No expenses found.")
            else:
                for i in expense:
                    print(f"Name: {i['name']}")
                    print(f"Amount: ₹{i['amount']}")
                    print(f"Date: {i['date'].strftime('%d-%m-%Y')}")
                    print(f"Category: {i['category']}")
                    print("--------------------")

        case 3:
            print("\n--- Save Expenses ---")

            file = open(FILE_PATH, 'w')

            for i in expense:
                store = (
                    f"{i['name']} | "
                    f"{i['amount']} | "
                    f"{i['date'].strftime('%d-%m-%Y')} | "
                    f"{i['category']}\n"
                )

                file.write(store)

            file.close()

            print("Expenses saved successfully!")

        case 4:
            print("\n--- Load Expenses ---")

            try:
                file = open(FILE_PATH, 'r')
                content = file.read()
                file.close()

                if content:
                    print(content)
                else:
                    print("No saved expenses found.")

            except FileNotFoundError:
                print("Expense file does not exist yet.")

        case 5:
            print("\n--- Monthly Total ---")

            total = 0

            month = int(input("Enter month number (1-12): "))

            for i in expense:
                if month == i['date'].month:
                    total = total + i['amount']

            print(f"Total expenses for month {month}: ₹{total}")

        case 6:
            print("\nExiting...")
            return False

        case _:
            print("Invalid choice. Please enter a number from 1 to 6.")


user_input = input("Do you want to start? (y/n): ")

while user_input == 'y':

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Save Expenses")
    print("4. Load Expenses")
    print("5. Monthly Total")
    print("6. Exit")

    code = int(input("Enter your choice: "))

    result = expense_tracker(code)

    if result == False:
        break

    user_input = input("\nDo you want to continue? (y/n): ")

print("Thank you for using Expense Tracker!")