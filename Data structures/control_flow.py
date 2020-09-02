
# Continue terminates an iteration
# Prints all letters except 'e' and 's'  
for letter in 'geeksforgeeks':  
    if letter == 'e' or letter == 's':  
        continue
    print('Current Letter :', letter) 
 
#########################################################
    
# we use the pass statement to construct a body that does nothing

for val in sequence:
    pass

def function(args):
    pass

class Example:
    pass

#########################################################

#enumerate()
for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']): 
    print(key, value)
    
#########################################################

# using zip() to combine two containers
questions = ['name', 'colour', 'shape'] 
answers = ['apple', 'red', 'a circle'] 
  
for question, answer in zip(questions, answers): 
    print('What is your {0}?  I am {1}.'.format(question, answer)) 
    
#########################################################

# python code to demonstrate working of items() 

king = {'Alexander': 'The Great', 'Solomon': 'The Wise', 'Aegeon': 'The Conqueror'} 
  
# using items to print the dictionary key-value pair 
for key, value in king.items(): 
    print(key, value) 
    
#########################################################

# Sorted()

lis = [ 1 , 3, 5, 6, 2, 1, 3 ] 

# using sorted() to print the list in sorted order 
print ("The list in sorted order is : ") 
for i in sorted(lis) : 
    print (i,end=" ") 
    
# And removing duplicates
print ("The list in sorted order (without duplicates) is : ") 
for i in sorted(set(lis)) : 
    print (i,end=" ") 

# Reverse list
print ("The list in reversed order is : ") 
for i in reversed(lis) : 
    print (i,end=" ") 

