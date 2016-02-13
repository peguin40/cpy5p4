#q1_sum_series1.py
#sums 1+1/2+....+1/n

# Defines function(Recursive function)

def sum_series1(i):
    if i==1:
        return 1 # Last value
    else:
        return 1/i+sum_series1(i-1) 

#get input
while True:
    try:
        i = int(input("Please enter an integer: "))
        break
    except ValueError as e:                         # Handling Exception if an invalid input was entered
        print("Errror"+e)

#main function
print(sum_series1(i))
