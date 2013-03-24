
ALLOWED_COMPOUND_PERIODS = [x for x in xrange(1, 13) if 12 % x == 0]
ALLOWED_PERIOD_PER_YEAR = [x for x in xrange(1, 13) if 12 % x == 0]


class Calculator():

    def __init__(self, **kwargs):
        self.initial_payment = kwargs['initial_payment'] or 0
        self.initial_amount = int(kwargs['initial_amount']) or 0
        self.annual_interest = kwargs['annual_interest'] or 0

        self.compound_period_per_year = kwargs.get('compound_period_per_year', 12)
        self.compound_period_per_year = self.compound_period_per_year if self.compound_period_per_year in ALLOWED_COMPOUND_PERIODS else 12

        self.payment_periods_per_year = kwargs.get('payment_periods_per_year', 12)
        self.payment_periods_per_year = self.payment_periods_per_year if self.payment_periods_per_year in ALLOWED_PERIOD_PER_YEAR else 12

        self.yearly_payment_increase_rate = kwargs.get('yearly_payment_increase_rate', 0)
        self.total_of_payments = 0

        # Determines wheter the interest are paid at the beginning, or the end of the period.
        # bom stand for beginning of period
        self.bop_interest_payment = kwargs.get('bop_interest_payment', True)

    def calc(self, nb_months):

        FV = 0
        payment = self.initial_payment
        Sum = self.initial_amount

        for period in xrange(1, nb_months + 1):

            # Is it a new year and do we increase payments ?
            if self.yearly_payment_increase_rate and period != 1 and (period - 1) % 12 == 0:
                    payment += (self.yearly_payment_increase_rate) * self.initial_payment

            #Do we receive interest ?
            if period % 12 / self.compound_period_per_year == 0:

                # time to make payment ?
                if period % 12 / self.payment_periods_per_year == 0:

                    #  Calculate interest on this periods payment also
                    if self.bop_interest_payment:
                        Sum = (Sum + payment) * (1 + self.annual_interest / self.compound_period_per_year)
                    else:
                        Sum = Sum * (1 + self.annual_interest / self.compound_period_per_year) + payment
                # We receive interests payments only.
                else:
                    Sum = Sum * (1 + self.annual_interest / self.compound_period_per_year)

            #no interest received this period. Lets check if its time to make a payment
            else:
                # time to make payment ?
                if period % 12 / self.payment_periods_per_year == 0:
                    Sum += payment
            print period, Sum
        return FV
