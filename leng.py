'''Find words which are greater than given length k'''
'''Find words which are greater than given length k'''
string1 = input("enter the string: ")
str_spl = string1.split()
k = int(input("enter the value of k :"))
empty =[]
for i in str_spl:
    if len(i) > k:
        empty.append(i)
if empty:
    print(empty)
else:
    print(" No words are found: ")
        