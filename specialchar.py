string =  input("enter the string ")
new_str ="$"
for i in string:
    if new_str in string:
        print("this string is not accepted:")
        break
else:
    print(string)
