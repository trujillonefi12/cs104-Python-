## by  nefi


def correctFloatingNumber(a, b):

    while True:
        try:
            userInput = float(input(a))
            return userInput
        except ValueError:
            print(b)


def main():
    transactions = []

    while True:
        # Menu for user choices
        print("\n1-Calculate net pay")
        print("2-Enter revenue or expense")
        print("3-Show discretionary income")
        print("4-Exit")
        choice = input("Choice: ")

        if choice == "1":
            calculate_net_pay(transactions)
        elif choice == "2":
            enter_transaction(transactions)
        elif choice == "3":
            show_discretionary_income(transactions)
        elif choice == "4":
            print("Thanks for using My Finance!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


def calculate_net_pay(transactions):
    hourly_wage = correctFloatingNumber(
        "What is your hourly wage?: ", "Please enter a number!"
    )
    hours_worked = correctFloatingNumber(
        "How many hours did you work?: ", "Please enter a number!"
    )

    gross_pay = hourly_wage * hours_worked
    federal_tax = gross_pay * 0.10
    state_tax = gross_pay * 0.05
    social_security = gross_pay * 0.062
    net_pay = gross_pay - federal_tax - state_tax - social_security

    print(
        f"\nGross Pay: ${gross_pay:.2f} ({hours_worked} hours @ ${hourly_wage:.2f}/hr)"
    )
    print(f"Federal tax: ${federal_tax:.2f}")
    print(f"State tax: ${state_tax:.2f}")
    print(f"Social security: ${social_security:.2f}")
    print(f"Net pay: ${net_pay:.2f}")

    transactions.append(("pay", net_pay))


def enter_transaction(transactions):
    while True:
        name = input("Enter transaction name: ")
        amount = correctFloatingNumber(
            "Enter amount (use negative sign for expense): ", "Please enter a number!"
        )
        transactions.append((name, amount))

        choice = input("Another? (Y/N): ").strip().lower()
        if choice != "y":
            break


def show_discretionary_income(transactions):
    revenue, expenses = 0, 0

    for name, amount in transactions:
        if amount >= 0:
            revenue += amount
        else:
            expenses += amount

    discretionary_income = revenue + expenses  # expenses are negative
    print(
        f"Revenue: ${revenue:.2f} Expenses: ${-expenses:.2f} Discretionary: ${discretionary_income:.2f}"
    )
