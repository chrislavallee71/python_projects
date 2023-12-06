import argparse
import math

parser = argparse.ArgumentParser(description="This calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal.")

parser.add_argument("--type", required=False, help="Payment type 'annuity' or 'diff' (differentiated)")
parser.add_argument("--payment", type=float, required=False, help="Payment amount")
parser.add_argument("--principal", type=float, required=False, help="Principal")
parser.add_argument("--periods", type=int, required=False, help="Number of months needed to repay the loan")
parser.add_argument("--interest", type=float, required=False, help="Interest rate")

args = parser.parse_args()

# Check for missing or invalid type
if args.type is None or args.type not in ("diff", "annuity"):
    print("Incorrect parameters")
    exit()
# Check for negative interest rate
elif args.interest is None:
    print("Incorrect parameters")
    exit()
    
# Check for negative values in payment, principal, periods, and interest
negative_args = [args.payment, args.principal, args.periods, args.interest]
if any(arg is not None and arg < 0 for arg in negative_args):
    print("Incorrect parameters")
    exit()



def calculator(payment, principal, periods, interest, type):
    over = 0  # Initialize overpayment variable outside the loop

    if args.interest is not None:
        interest_rate = float(args.interest)
        i = interest_rate / (12 * 100)  # nominal (monthly) interest rate

    # Check which argument is missing and calculate it
    if periods is None:
        # Calculate the number of periods
        n = math.log(payment / (payment - i * principal)) / math.log(1 + i)
        periods = math.ceil(n)
        years, months = divmod(periods, 12)
        p_total = payment * periods
        over = p_total - principal
        if years > 1 and months > 1:
            print(f"It will take {years} years and {months} months to repay this loan!")
        elif years > 1:
            print(f"It will take {years} years to repay this loan!")
        elif months > 1:
            print(f"It will take {months} months to repay this loan!")
        else:
            print("It will take 1 month to repay this loan!")
    elif payment is None:
        # Calculate annuity payment
        if type == "annuity":
            # Calculate the monthly payment
            pay = principal * (((i * math.pow(1 + i, periods))) / (math.pow(1 + i, periods) - 1))
            pay_total = math.ceil(pay) * periods
            over = pay_total - principal
            print(f"Your annuity payment = {int(math.ceil(pay))}!")
        # Calculate differentiated payment
        elif type == "diff":
            # Calculate the monthly payment
            pay_total = 0
            for m in range(1, periods + 1):
                pay = (principal / periods) + (i * ( (principal - ((principal * (m - 1)) / periods))))
                pay_total += math.ceil(pay)
                print(f"Month {m}: payment is {int(math.ceil(pay))}")
                over = pay_total - principal
        else:
            print("Incorrect parameters")
    elif principal is None:
        # Calculate the loan principal
        principal = payment / (((i * math.pow(1 + i, periods))) / (math.pow(1 + i, periods) - 1))
        print(f"Your loan principal = {int(math.ceil(principal))}!")
        pay = principal * (((i * math.pow(1 + i, periods))) / (math.pow(1 + i, periods) - 1))
        pay_total = math.ceil(pay) * periods
        over = pay_total - principal
    # Type not specified 
    else:
        print("Incorrect parameters")

    # Print the overpayment outside the if-else block
    print(f"Overpayment = {math.ceil(over)}")

# Call the calculator function with arguments from the command line
calculator(args.payment, args.principal, args.periods, args.interest, args.type)
