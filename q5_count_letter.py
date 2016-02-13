#q5_count_letter.py
# recursive function that finds character in string

#Define Function

def count_letter(string,ch):
    if string.find(ch)==-1:
        return 0
    else:
        if string.find(ch)==0:
            string = string[1:]
        else:
            string = string[:string.find(ch)-1]+string[string.find(ch)+1:]
        return 1+count_letter(string,ch)

# get inputs
while True:
    try:
        string = str(input("Please enter a string: "))
        ch = str(input("Please enter a character: "))
        break
    except Exception as e:
        print(e)

# main
print(count_letter(string,ch))
