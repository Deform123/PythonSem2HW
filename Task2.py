#Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

n = int(input("Введите число : "))

for i in range(2, n+1):
    if n % i == 0:
        print(f"Наименьший натуральный делитель введенного вами числа - {i}")
        break