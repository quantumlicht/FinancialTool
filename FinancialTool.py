
import argparse
from calculator import Calculator

parser = argparse.ArgumentParser()
parser.add_argument('nb_periods', help='Number of months for the calculation')
parser.add_argument('payment', help='Initial payment', type=float)
parser.add_argument('-i', "--init", help='Initial cash', type=float, default=0)
parser.add_argument('interest', help='Annual interest rate', type=float)
parser.add_argument('-c', "--compY", help='Number of compound periods per year', type=int, default=12)
parser.add_argument('-p', '--paymentY', help='Number of payment periods per year', type=int, default=12)
parser.add_argument('-y', "--payIncY", help='Yearly increase in payments', default=0, type=float)
parser.add_argument('-b', "--bop", help='Flag to decide if we pay interest at the beginning of the period', action='store_true', default=False)

args = parser.parse_args()


calc = Calculator(**{
    'initial_payment': args.payment,
    'initial_amount': args.init,
    'annual_interest': args.interest,
    'compound_period_per_year': args.compY,
    'payment_periods_per_year': args.paymentY,
    'yearly_payment_increase_rate': args.payIncY,
    'bop_interest_payment': args.bop})

test = calc.calc(int(args.nb_periods))
