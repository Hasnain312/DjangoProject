from django.shortcuts import render

# Create your views here.
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

def subtract(a, b):
    return a - b

print(subtract(10, 5))