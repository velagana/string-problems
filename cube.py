'''Python program to create a list of tuples from given list having number and its cube in each tuple'''
list1 = [1,2,3,4]
result  =  [(val,pow(val,3)) for val in list1]
print(result)