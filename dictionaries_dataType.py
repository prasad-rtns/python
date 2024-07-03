# Dictionaries
my_stuff = {"key1":"value1", "key2":123, "key3":True, "key4":{'123':[1,2,'abc']}}
print(my_stuff["key4"]['123'][2])
print(my_stuff["key3"])
print(my_stuff["key2"])

my_dict = {'lunch':'pizza', 'bfast':'eggs'}
print(my_dict['lunch'])
my_dict['lunch'] = 'burger'
print(my_dict)
my_dict['dinner'] = 'meat'
print(my_dict)

## DATA TYPES
# Tuples
t = (1,2,3)
print(t[0])
#t[0] = "New"  ### -> ERROR TypeError: 'tuple' object does not support item assignment

# Booleans
# -> True / False / 0 / 1

# SETS
x = set()

x.add(1)
x.add(2)
x.add(0.2)
print(x) # {0.2, 1, 2} -> Set is unorder and only take unique elements