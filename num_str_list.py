# Numbers
my_income = 500
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)

# String
mystring = 'TestString'
print(mystring)
print(mystring[2]) # s
print(mystring[2:]) # stString 
print(mystring[:3]) # Tes 
print(mystring[2:6]) # stSt 
print(mystring[::1]) # TestString
print(mystring[::2]) # TsSrn
print(mystring[::-1]) # gnirtStseT -> Reverse

string = 'Hello World'
x = string.split() # ['Hello', 'World']
print(x)

# Print Formatting
item = "Item one: {} Item two: {}".format("dog", "cat")
item = "Item one: {x} Item two: {y}".format(x = "dog", y = "cat")
print(item)

#Lists
mylist = [1,2,3]
mylist = ['string', 1, 2, 3, True, [1,2,3]]
print(mylist[0]) # string
print(len(mylist)) # 6

mylist_1 = ['a', 'b', 'c', 'd', 'e']
print(mylist_1)
mylist_1[0] = "Update a"
print(mylist_1)
mylist_1.append('NewItem')
print(mylist_1)

listtwo = ['x', 'y', 'z']
mylist_1.append(listtwo)
print(mylist_1)
mylist_1.extend(listtwo)
print(mylist_1)

itempop = mylist_1.pop()
print(mylist_1)
print(itempop)
listtwo.reverse()
print(listtwo)

# Nested List
nestedList = [1, 2, ['x', 'y', 'z']]
print(nestedList[2][1]) # y

#List Comprehension
matrix = [[1,2,3], ['a','b','c'], [4,5,6]]
first_col = [row[0] for row in matrix]
print(first_col) # [1, 'a', 4]