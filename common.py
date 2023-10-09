string1 = "abcdef"
string2 ="efabgh"
empty = " "
for i in string1:
    if i in string2:
        empty = empty + i
print(empty)