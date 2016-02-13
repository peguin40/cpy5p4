#q2_sum_series2.py
# Sum a series 1/3 + 2/5 +.... + i/(2i+1)

# Define Function

def sum_series2(i):
    if i == 1:
        return 1/3
    else:
        return i/(2*i+1)+sum_series2(i-1)

# get input

while True:
    try:
        i = int(input("Please enter an integer: "))
        break
    except ValueError as e:
        print(e)

# main

print(sum_series2(i))
