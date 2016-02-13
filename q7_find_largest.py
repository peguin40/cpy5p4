#q7_find_largest.py
# finds largest integer in an array

#Define Function
def find_largest(alist):
    if len(alist)<2:
        return alist[0]
    elif alist[0]>alist[1] and len(alist)==2:
        return alist[0]
    elif alist[0]>alist[1] and len(alist)>2:
        del alist[1]
        return find_largest(alist)
    else:
        del alist[0]
        return find_largest(alist)

# get input list
alist = input("Please enter a list: ").split(",")

# main

print(find_largest(alist))
