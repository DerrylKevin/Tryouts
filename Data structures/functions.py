# Functions

# *args for variable number of arguments 
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')  

# *kargs for variable number of keyword arguments 
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks') 
    

def myFun(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
# Now we can use *args or **kwargs to pass arguments to this function :  
args = ("Geeks", "for", "Geeks") 
myFun(*args) 

kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
myFun(**kwargs) 


def myFun(*args,**kwargs): 
    print("args: ", args) 
    print("kwargs: ", kwargs) 
# Now we can use both *args ,**kwargs to pass arguments to this function : 
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks") 

####################################################

# Yield 
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 
    
'''
Yield are used in Python generators. A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return.
'''

# An infinite generator function that prints next square number. It starts with 1 
def nextSquare(): 
    i = 1; 
    # An Infinite loop to generate squares  
    while True: 
        yield i*i                 
        i += 1  # Next execution resumes from this point      
# Driver code to test above generator function 
for num in nextSquare(): 
    if num > 100: 
         break    
    print(num) 

# Generator functions
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
    
# x is a generator object 
x = simpleGeneratorFun() 
# Iterating over the generator object using next 
print(x.__next__())  
print(x.__next__()) 
print(x.__next__()) 


# A simple generator for Fibonacci Numbers 
def fib(limit): 
    # Initialize first two Fibonacci Numbers  
    a, b = 0, 1
    # One by one yield next Fibonacci Number 
    while a < limit: 
        yield a 
        a, b = b, a + b 
# Create a generator object 
x = fib(5) 
# Iterating over the generator object using next 
print(x.__next__()) 
print(x.__next__()) 
print(x.__next__()) 
print(x.__next__()) 
print(x.__next__()) 
  
# Iterating over the generator object using for loop. 
for i in fib(5):  
    print(i) 

####################################################

# Anonymous functions a.k.a labmda function  
cube = lambda x: x*x*x  
print(cube(7))


def power(n): 
    return lambda a : a ** n 
  
# base = lambda a : a**2 get returned to base 
base = power(2) 
print("Now power is set to 2") 
  
# when calling base it gets executed with already set with 2 
print("8 powerof 2 = ", base(8)) 

base = power(5) 
print("Now power is set to 5") 
print("8 powerof 5 = ", base(8)) 


#lambda functions inside map() and filter() 
a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11] 
  
filtered = filter (lambda x: x % 2 == 0, a)  
print(list(filtered)) 

maped = map (lambda x: x % 2 == 0, a)  
print(list(maped)) 

######################################################

# First Class functions in Python

# 1. Function treated as objects
def shout(text): 
    return text.upper() 
  
print(shout('Hello'))
yell = shout                # As object
print(yell('Hello'))

# 2. Functions as arguments

def shout(text): 
    return text.upper() 
  
def whisper(text): 
    return text.lower() 
  
def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a function passed as an argument.") 
    print greeting  
  
greet(shout) 
greet(whisper) 


# 3. Functions can return another function 

def create_adder(x): 
    def adder(y): 
        return x+y 
    return adder 
  
add_15 = create_adder(15)
print add_15(10)

######################################################

# Decorators

# Higher Order Functions are function that returns or accepts another function as argument
def greet(func):
    func()
# OR
def greet2():
    def func():
        return 5
    return func

# decorator try 1 
def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func

@my_decorator
def hello():                    
    print('helloooo')

def bye():                      
    print('see you later')

hello()               #with decorator
bye()                 #without decorator

# Here's what's happening in the background
def hello2():                    
    print('helloooo')
a = my_decorator(hello2)
a()
my_decorator(hello2)()

# decorator try 2
def my_decorator(func):
    def wrap_func(x):
        print('********')
        func(x)
        print('********')
    return wrap_func

@my_decorator
def hello(greeting):
    print(greeting)

hello('hiii')

# decorator try 3
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('********')
    return wrap_func

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)

hello('hiii')

# Decorators example application

from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*5
        
long_time() 
