''' Python | Check if a given string is binary string or not'''
string1 = input("enter the string: ")
is_binary = True
for i in string1:
     if i != '0' and i != '1':
         is_binary = False
if is_binary:
    print(string1)
else:
    print("not an accepted string")
     