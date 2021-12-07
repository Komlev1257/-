from random import randint
mas = []
for i in range(100):
    mas.append(randint(1, 100))


def check(a, b, c):
    if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
        return True
    else:
        return False


def area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
    return s


allarea = []
for i in range(len(mas) - 2):
    a = mas[i]
    b = mas[i + 1]
    c = mas[i + 2]
    allarea.append(area(a, b, c))
    if check(a, b, c) == True:
        print("a = ", a, "b = ", b, "c = ", c, "Площадь = ", area(a, b, c))
    else:
        print("Такой треугольник не существует")

for i in range(len(allarea)):
    if type(allarea[i]) == complex:
        allarea[i] = 0

print(allarea)
print("Максимальная площадь = ", max(allarea))
