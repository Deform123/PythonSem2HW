#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input("Введите число : "))
list = []
factorial = 1
for i in range(1, num + 1):
    factorial *= i
    list.append(factorial)
print(list)