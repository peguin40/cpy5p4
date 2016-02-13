#q8_find_uppercase.py
#finds number of uppercase letters in string

#define function

def find_num_uppercase(string):
    if len(string)==0:
        return 0
    elif string[0].isupper()==False:
        return find_num_uppercase(string[1:])
    else:
        return 1+find_num_uppercase(string[1:])

# get input
while True:
    try:
        string = input("Please enter a string: ")
        break
    except Exception as e:
        print(e)

#main
print(find_num_uppercase(string))
