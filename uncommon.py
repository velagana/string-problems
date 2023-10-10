string1 = input("Enter the string: ").split()
string2  = input("Enter the string: ").split()
app = []
for i in string1:
    if i not in string2:
        app.append(i)
for i in string2:
    if i not in string1:
        app.append(i)
print(i)
        


