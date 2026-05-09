''' FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''

print("===== DEFINE (Parameters) vs CALL (Arguments) =====")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - build: def keyword is a and b parameters
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute: the arguments are martin and justin
result1 = greet('Martin')
print("result1:", result1)

result2 = greeting('Justin')
print("result2:", result2)

print("===== Keyword & Default Arguments =====")
# Keyword arguments: name=value


def give_greet(name, age):  # age=22 # default argument and will be printed 22 if age is not provided
    return f"Hello, {name}! You are {age} years old."


# CALL - execute: the arguments are martin and justin
result3 = give_greet('Martin', 25)
print("result3:", result3)

result4 = give_greet(age=30, name='Justin')
print("result4:", result4)


print("===== Scope =====")
# Scope: where a variable is accessible
# Local scope: variables defined inside a function
b = 100  # Global scope: variables defined outside any function
# 3


def calculate(a, b):  # 2
    c = a * b  # 1
    print(f"the c value is: {c}")


calculate(5, 50)
