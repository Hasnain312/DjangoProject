from django.shortcuts import render

# Create your views here.
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

def subtract(a, b):
    return a - b

print(subtract(10, 5))

def add(a, b):
    return a + b

result = add(30, 40)
print(result)


def subtract(a, b):
    return a - b

print(subtract(80, 50))

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b

print(divide(10, 2))
print(divide(10, 0))