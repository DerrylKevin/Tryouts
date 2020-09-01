# Formatting of Strings 
  
# Default order 
String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
print("Print String in default order: ") 
print(String1) 
  
# Positional Formatting 
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
print("\nPrint String in Positional order: ") 
print(String1) 
  
# Keyword Formatting 
String1 = "{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life') 
print("\nPrint String in order of Keywords: ") 
print(String1)

###########################################################

# Formatting of Integers 
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1) 
  
# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1) 
  
# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1) 

###########################################################

# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1)
  
# To demonstrate aligning of spaces  
String1 = "\n{0:^20} was founded in {1:<4}!".format("GeeksforGeeks", 2009) 
print(String1) 

###########################################################

# Old Style Formatting of Integers 
  
Integer1 = 12.3456789
print("Formatting in 3.2f format: ") 
print('The value of Integer1 is %3.2f' %Integer1) 
print("\nFormatting in 3.4f format: ") 
print('The value of Integer1 is %3.4f' %Integer1) 

###########################################################

# Addition of Element at specific Position (using Insert Method) 
List = [1,2,3,4] 
List.insert(3, 12) 
List.insert(0, 'Geeks') 
print("\nList after performing Insert Operation: ") 
print(List) 
 
# Addition of multiple elements to the List at the end (using Extend Method) 
List = [1,2,3,4]
List.extend([8, 'Geek', 'Always']) 
print("\nList after performing Extend Operation: ") 
print(List) 

#  Removing elements using remove and pop
List = [1,3,5,10]
List.remove(10)
print(List)
print(List.pop(1))

###########################################################

#List Methods
Function 	Description
Append() 	Add an element to the end of the list
Extend() 	Add all elements of a list to the another list
Insert() 	Insert an item at the defined index
Remove() 	Removes an item from the list
Pop() 	    Removes and returns an element at the given index
Clear() 	Removes all items from the list
Index() 	Returns the index of the first matched item
Count() 	Returns the count of number of items passed as an argument
Sort() 	    Sort items in a list in ascending order
Reverse() 	Reverse the order of items in the list
copy() 	    Returns a copy of the list


#Built-in functions with List
Function 	Description
reduce() 	apply a particular function passed in its argument to all of the list elements stores the intermediate result and only returns the final summation value
sum() 	Sums up the numbers in the list
ord() 	Returns an integer representing the Unicode code point of the given Unicode character
cmp() 	This function returns 1, if first list is “greater” than second list
max() 	return maximum element of given list
min() 	return minimum element of given list
all() 	Returns true if all element are true or if list is empty
any() 	return true if any element of the list is true. if list is empty, return false
len() 	Returns length of the list or size of the list
enumerate() 	Returns enumerate object of list
accumulate() 	apply a particular function passed in its argument to all of the list elements returns a list containing the intermediate results
filter() 	tests if each element of a list true or not
map() 	returns a list of the results after applying the given function to each item of a given iterable
lambda() 	This function can have any number of arguments but only one expression, which is evaluated and returned.

###########################################################

# Tuples can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple.
Tuple1 = tuple('GEEKSFORGEEKS')
print(Tuple1[::-1])

#Tuple unpacking 
Tuple1 = ("Geeks", "For", "Geeks") 

# Concatenaton of tuples 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('Geeks', 'For', 'Geeks') 
Tuple3 = Tuple1 + Tuple2 

# Deleting a Tuple 
Tuple1 = (0, 1, 2, 3, 4) 
del Tuple1 

#Built-In Methods
Built-in Function 	Description
all() 	Returns true if all element are true or if tuple is empty
any() 	return true if any element of the tuple is true. if tuple is empty, return false
len() 	Returns length of the tuple or size of the tuple
enumerate() 	Returns enumerate object of tuple
max() 	return maximum element of given tuple
min() 	return minimum element of given tuple
sum() 	Sums up the numbers in the tuple
sorted() 	input elements in the tuple and return a new sorted list
tuple() 	Convert an iterable to a tuple.

###########################################################

# Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print(set1)

# Adding elements Using add() method
set1 = set()
print(set1)
set1.add(8) 
set1.add(9) 
set1.add((6,7)) 
print(set1) 

#For addition of two or more elements Update() method is used
set1 = set([ 4, 5, (6, 7)])     
set1.update([10, 11]) 
print(set1) 

'''
Removing elements from the Set
Using remove() method or discard() method

Elements can be removed from the Set by using built-in remove() 
function but a KeyError arises if element doesn’t exist in the set. 
To remove elements from a set without KeyError, use discard()
'''

set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) 
set1.remove(5) 
set1.discard(8) 
set1.pop()              #pops a random element
set1.clear()            #remove all the elements

'''While elements of a set can be modified at any time, 
elements of the frozen set remain the same after creation.
'''
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r') 
Fset1 = frozenset(String) 


#Set Methods
Function 	Description
add() 	    Adds an element to a set
remove() 	Removes an element from a set. If the element is not present in the set, raise a KeyError
clear() 	Removes all elements form a set
copy() 	    Returns a shallow copy of a set
pop() 	    Removes and returns an arbitrary set element. Raise KeyError if the set is empty
update() 	Updates a set with the union of itself and others
union() 	Returns the union of sets in a new set
difference() 	Returns the difference of two or more sets as a new set
difference_update() 	Removes all elements of another set from this set
discard() 	Removes an element from set if it is a member. (Do nothing if the element is not in set)
intersection() 	Returns the intersection of two sets as a new set
intersection_update() 	Updates the set with the intersection of itself and another
isdisjoint() 	Returns True if two sets have a null intersection
issubset() 	Returns True if another set contains this set
issuperset() 	Returns True if this set contains another set
symmetric_difference() 	Returns the symmetric difference of two sets as a new set
symmetric_difference_update() 	Updates a set with the symmetric difference of itself and another

###########################################################

# Dictionary
Dict = {} 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
Dict['Value_set'] = 2, 3, 4   # Adding a set of vaules to a single key
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}}  #Adding a Nested Key
print(Dict) 
  
# Creating a Dictionary with dict() method 
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
  
# Creating a Dictionary with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 


print(Dict[1])          #Accessing with key
print(Dict.get(3))      #Accessing with get()

# Deleting  
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}, 
        'B' : {1 : 'Geeks', 2 : 'Life'}} 
del Dict[6]         #Deleting a Key value
del Dict['A'][2]        #Deleting a key from Nested Dictionary
pop_ele = Dict.pop(1)   # Deleting a key using pop() method 
pop_ele = Dict.popitem() # Deleting an arbitrary key using popitem() function  
Dict.clear()        # Deleting entire Dictionary


#Dictionary Methods
Methods 	Description
copy() 	They copy() method returns a shallow copy of the dictionary.
clear() 	The clear() method removes all items from the dictionary.
pop() 	Removes and returns an element from a dictionary having the given key.
popitem() 	Removes the arbitrary key-value pair from the dictionary and returns it as tuple.
get() 	It is a conventional method to access a value for a key.
dictionary_name.values() 	returns a list of all the values available in a given dictionary.
str() 	Produces a printable string representation of a dictionary.
update() 	Adds dictionary dict2’s key-values pairs to dict
setdefault() 	Set dict[key]=default if key is not already in dict
keys() 	Returns list of dictionary dict’s keys
items() 	Returns a list of dict’s (key, value) tuple pairs
has_key() 	Returns true if key in dictionary dict, false otherwise
fromkeys() 	Create a new dictionary with keys from seq and values set to value.
type() 	Returns the type of the passed variable.
cmp() 	Compares elements of both dict.

###########################################################

#Array
 
import array as arr 
  
# creating an array with integer type 
a = arr.array('i', [1, 2, 3]) 
  
# creating an array with float type 
b = arr.array('d', [2.5, 3.2, 3.3]) 
  
# Adding Elements to a Array
a.insert(1, 4)          # using insert()
b.append(4.4)           # using append()

# Accessing elements same as lists

# Remove() method only removes the occurence of an element. 
# pop() function used to remove element in an index

print (a.index(2))  # searching occurence of 2 in array

