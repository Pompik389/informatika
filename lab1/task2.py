from math import sin, cos, log, exp
x = float(input("введите значение переменной x: "))
y = float(input("введите значение переменной y: "))
z = float(input("введите значение переменной z: "))
a=(x**3/2)**0.5-sin(y)
b=exp(2)/3-cos(y)+z+log(y)
print(f"Получено значение функции a={a}")
print(f"Получено значение функции b={b}")
