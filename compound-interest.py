#!/usr/bin/env python

# Calculate compound interest amount with amount, interest rate,
# time and compounding time
#
# Set up: None
#
# Command line inputs: None
# In file inputs: None
# Runtime inputs: Yes

p = 0
n = 0
d = 0
r = 0

def get_input():
    global p,n,r,d
    amount_str = raw_input('Enter the amount: ')
    p = float(amount_str)
    interest_str = raw_input('Enter the interest: ')
    r = float(interest_str)
    time_str = raw_input('Enter the time in years: ')
    n = float(time_str)
    calculate_str = raw_input('Enter the compunding time in months: ')
    d = float(calculate_str)

def calculate_yr(mon):
    global p,r,d
    times = int(mon/d)
    while times > 0:
        val = (p * r * 0.01 * d)/12
        p = p + val
        times = times - 1
        
def calculate():
    global n
    if n < 1.0:
        calculate_yr(12 * n)
    elif n >= 1.0:
        times = int(n)
        while times > 0:
            calculate_yr(12)
            times = times - 1
            
if __name__ == "__main__":
    get_input()
    calculate()
    print "Final amount: " + str(p)