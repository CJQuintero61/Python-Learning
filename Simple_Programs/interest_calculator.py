# calculate interest based on user input

# daily periods
PERIODS = 365

def calculate_interest(principle: float, rate: float, time: int) -> float:
    # calculates interest based on user input
    #
    # params:
    #       principle: float - the principle amount
    #       rate: float - the interest rate
    #       time: int - the number of years
    #
    # returns:
    #       float - the calculated final amount after interest

    result = principle * ((1 + (rate/PERIODS)) ** (PERIODS * time))
    return result

rate = float(input('Enter the rate: '))
while rate <= 0:
    print('Invalid rate\n')
    rate = int(input('Enter the rate: '))

time = int(input('Enter the number of years: '))
while time <= 0:
    print('Invalid time\n')
    time = int(input('Enter the number of years: '))

principle = float(input('Enter the principle: '))
while principle <= 0:
    print('Invalid principle\n')
    principle = float(input('Enter the principle: '))

result = calculate_interest(principle, rate, time)
print(f'The total is {result}')