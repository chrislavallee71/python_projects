#  Create a simple tool that will calculate your net income

shop_gross = {'Bubblegum': 202, 'Toffee': 118, 'Ice cream': 2250, 'Milk chocolate': 1680, 'Doughnut': 1075, 'Pancake': 80}

def earn_amt(n: dict[str, float | int]) -> None:
    print('Earned amount:')
    # Print each item and its sales
    [print(f'{item}: ${sales}') for item, sales in n.items()]
    
    # Calculate the total income and print it
    total_income = sum(n.values())
    print(f'\nIncome: ${total_income}')
    return total_income

# Get total income
total_income = earn_amt(shop_gross)

# Input staff and other expenses
print("Staff expenses:")
staff_exp = float(input())

print("Other expenses:")
other_exp = float(input())

# Calculate total expenses and net income
total_exp = staff_exp + other_exp
shop_net = total_income - total_exp

# Print the net income
print(f"Net income: ${shop_net:.2f}")
