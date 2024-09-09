# Основные конструкции Python:
print("Hello, Automation Testing!")

x = 10
y = 5
print(x + y)
print(x - y)

if x > y:
    print("x больше y")
else:
    print("x меньше или равен y")

for i in range(5):
    print(i)

#Функции и модули:

def greet(name):
    return f"Hello, {name}!"
print(greet("world"))

import math
print(math.sqrt(15))