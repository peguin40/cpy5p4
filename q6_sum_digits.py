#q6_sum_digits.py
#sums the digits in an integer

# Define Function
def sum_digits(n):
    if n<10:
        return n
    else:
        return n%10 + sum_digits(n//10)

# get input
while True:
    try:
        n = int(input("Please enter an integer: "))
        break
    except ValueError as e:
        print(e)

# main
print(sum_digits(n))
