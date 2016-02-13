#q3_find_gcd.py
# Finds greatest common divisor of 2 numbers

# Define function

def gcd(m,n):
    if (m%n) == 0:
        return n
    else:
        return gcd(n,m%n)

# get inputs

while True:
    try:
        m=int(input("Please enter the 1st integer: "))
        n=int(input("Please enter the 2nd integer: "))
        break
    except ValueError as e:
        print(e)

# main

print(gcd(m,n))
