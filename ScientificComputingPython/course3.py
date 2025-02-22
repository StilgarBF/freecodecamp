def add_expense(expenses: list, amount: float, category: str) -> None:
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses: list) -> None:
    """
    Prints the amount and category of each expense in the given list.

    Args:
        expenses (list of dict): A list of dictionaries where each dictionary
                                 represents an expense with keys 'amount' and 'category'.

    Example:
        expenses = [
            {"amount": 50, "category": "Food"},
            {"amount": 20, "category": "Transport"}
        ]
        print_expenses(expenses)
        # Output:
        # Amount: 50, Category: Food
        # Amount: 20, Category: Transport
    """
    # Iterate through each expense and print its details
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses: list) -> float:
    """
    Calculate the total expenses from a list of expense dictionaries.

    Args:
        expenses (list): A list of dictionaries where each dictionary represents an expense.
                         Each dictionary should have an 'amount' key with a numeric value.

    Returns:
        float: The sum of all expense amounts.
    """
    # Sum the 'amount' values from all expense dictionaries in the list
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses: list, category: str) -> list:
    """
    Filters a list of expenses by a given category.

    Args:
        expenses (list): A list of expense dictionaries. Each dictionary should have a 'category' key.
        category (str): The category to filter expenses by.

    Returns:
        list: A list containing expenses that match the given category.
    """
    # Filter expenses based on the provided category
    return list(filter(lambda expense: expense['category'] == category, expenses))

def main():
    """
    Main function to run the Expense Tracker application.
    This function provides a menu-driven interface for users to:
    1. Add an expense
    2. List all expenses
    3. Show total expenses
    4. Filter expenses by category
    5. Exit the application
    The function continuously prompts the user for input until the user chooses to exit.
    Functions:
    - add_expense(expenses, amount, category): Adds a new expense to the list.
    - print_expenses(expenses): Prints all expenses in the list.
    - total_expenses(expenses): Calculates and returns the total of all expenses.
    - filter_expenses_by_category(expenses, category): Filters and returns expenses by the specified category.
    """
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
        elif choice == '5':
            print('Exiting the program.')
            break

main()
