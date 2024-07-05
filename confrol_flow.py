# conditions
if 1<2:
    print('Yes !')
    
if 1<2:
    print('Yes 1 !')    
    if 2 < 3:
        print('Yes 2 !')
        
if 1 > 2:
    print('Hello')
else:
    print('Else')

if 1 == 1:    
    if 1 > 2:
        print('Hello')
    elif 3 == 3:
        print('ElIf Run')
    else:
        print('Else')
        
## LOOPS
# For Loops

seq = [1,2,3,4,5]
for item in seq:
    print(item)  

d = {'sam':1, 'Frank':2}
for k in d:
    print(k)
    print(d[k])
    
mypairs = [(1,2), (3,4), (5,6)]
for tup1, tup2 in mypairs:
    print(tup2)
    print(tup1)
    
# While Loop
i = 1 
while i<5:
    print('i is : {}'.format(i))
    i = i+1
    
# Range
print(range(5)) # range(0, 5)
print(list(range(0,5))) # [0, 1, 2, 3, 4]
print(list(range(0,20,2))) #  [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

for item in range(5):
    print(item)
    
#List Comprehension
x = [1,2,3,4]

out = []
for num in x:
    out.append(num**2)
print(out)

out = [num**2 for num in x]
print(out)