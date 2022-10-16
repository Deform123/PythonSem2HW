#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

num = int(input("Введите число : "))
list = []
for i in range(-num, num + 1):
    list.append(i)
print(list)

elements = []
for i in input("Введите индексы элементов списка : ").split():
    elements.append(int(i))

product = 1
for index in elements:
    product *= list[index]
print(f"Произведение элементов списка под введенными Вами индексами равно - {product}")