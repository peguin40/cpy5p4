#q4_print_reverse.py
# reverses an integer

def reverse_int(n):
    if int(n)<10:
        return str(n)
    else:
        return str(n%10)+reverse_int(n//10)


# get inputs

while True:
    try:
        n = int(input("Please enter an integer: "))
        break
    except ValueError as e:
        print(e)

# main

print(reverse_int(n))
