# Bitwise operators
a = 10
b = 4
print(a & b)            #bitwise AND
print(a | b)            #bitwise OR
print(~a)               #bitwise NOT
print(a ^ b)            #bitwise XOR
print(a >> 2)           #bitwise right shift
print(a << 2)           #bitwise left shift


# Any , All
print (any([False, True, False, False]))
print (any([False, False, False, False]))
print (all([False, True, True, False]))


# Check if a number is divisible by 5
list1 = [i for i in range(20)]
list2 = []
for num in list1:
    list2.append(num%5 == 0)
print(any(list2))


# Difference between == and is
list1 = []
list2 = []
list3 = list1
print(list1 == list2)
print(list1 is list2)
print(list1 == list3)
print(list1 is list3)


# Python Membership and Identity Operators | in, not in, is, is not
1 in [0,1,2,3]
1 not in [0,1,2,3]

x = 5; y = 5.5
type(x) is int
type(y) is not int
