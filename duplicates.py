''' remove the duplicates from the string'''
string = input("enter the string : ")
new_str = " ";
for i in string:
    if i not in new_str:
        new_str = new_str + i
print(new_str)