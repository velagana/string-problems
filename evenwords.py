''' python programme to print the even length words'''
string = input("Enter the values of string: ")
len_str=string.split(" ")
for i in len_str:
    if len(i) % 2 == 0:
      print(i)