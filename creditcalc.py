import math
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, choices=['annuity', 'diff'], help='Incorrect parameters')
parser.add_argument("--principal", type=float)
parser.add_argument("--payment", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args(sys.argv[1:])


def user_choice(args) -> None:
    if args.type == 'annuity' and args.principal and args.payment and args.interest:
        monthly_payments(args)
    elif args.type == 'annuity' and args.principal and args.periods and args.interest:
        annuity_payment(args)
    elif args.type == 'annuity' and args.payment and args.periods and args.interest:
        loan_principal(args)
    elif args.type == "diff" and args.principal and args.periods and args.interest:
        different_payment(args)
    else:
        print("Incorrect parameters")


def monthly_payments(args) -> None:
    loan_principal = args.principal
    monthly_payment = args.payment
    loan_interest = args.interest
    interest = float(loan_interest / (100 * 12))
    number_of_mounts = math.ceil(
        math.log((monthly_payment / (monthly_payment - interest * loan_principal)), (1 + interest)))
    overpayment = monthly_payment * number_of_mounts - loan_principal
    if number_of_mounts == 12:
        print(f'It will take 1 year to repay this loan!\nOverpayment = {round(overpayment)}')
    elif number_of_mounts == 1:
        print(f'It will take {number_of_mounts} month to repay this loan!\nOverpayment = {round(overpayment)}')
    elif number_of_mounts < 12:
        months = number_of_mounts
        print(f'It will take {months} months to repay this loan!\nOverpayment = {round(overpayment)}')
    elif number_of_mounts % 12 == 0:
        year = round(number_of_mounts / 12)
        print(f'It will take {year} years to repay this loan!\nOverpayment = {round(overpayment)}')
    elif number_of_mounts % 12 >= 1:
        year = number_of_mounts // 12
        months = number_of_mounts % 12
        print(f'It will take {year} years and {months} months to repay this loan!\nOverpayment = {round(overpayment)}')


def annuity_payment(args) -> None:
    loan_principal = args.principal
    number_periods = args.periods
    loan_interest = args.interest
    interest = loan_interest / (100 * 12)
    divisible = interest * (math.pow((1 + interest), number_periods))
    divider = math.pow((1 + interest), number_periods) - 1
    annuity_payment = math.ceil(loan_principal * (divisible / divider))
    overpayment = annuity_payment * number_periods - loan_principal
    print(f'Your monthly payment = {annuity_payment}!\nOverpayment = {round(overpayment)}')


def loan_principal(args) -> None:
    annui_pay = args.payment
    number_periods = args.periods
    loan_interest = args.interest
    interest = loan_interest / (100 * 12)
    divisible = interest * (math.pow((1 + interest), number_periods))
    divider = math.pow((1 + interest), number_periods) - 1
    loan_principal = round(annui_pay / (divisible / divider))
    overpayment = annui_pay * number_periods - loan_principal
    print(f'Your loan principal = {loan_principal}!\nOverpayment = {round(overpayment)}')


def different_payment(args)->None:
    loan_principal = args.principal
    number_periods = args.periods
    loan_interest = args.interest
    interest = loan_interest / (100 * 12)
    month_counter = 0
    for date in range(1, number_periods + 1):
        num = math.ceil((loan_principal / number_periods) + interest * (
                loan_principal - ((loan_principal * (date - 1)) / number_periods)))
        month_counter += num
        payment = math.ceil((loan_principal / number_periods) + interest * (
            (loan_principal - (loan_principal * (date - 1)) / number_periods)))
        print(
            f'Month {date} payment is {payment}')
    print(f'Overpayment = {month_counter - loan_principal}')


user_choice(args)

