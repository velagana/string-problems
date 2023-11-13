''' Remove multiple elements from a list in Python'''
list = [ 2,4,5,6,7]
for i in list:
    if i % 2 == 0:
        list.remove(i)
        print(list)