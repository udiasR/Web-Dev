import math

# Вводим числа
a = int(input())
b = int(input())

# Находим первый корень, который даст полный квадрат >= a
start = math.ceil(math.sqrt(a))
# Находим последний корень, который даст полный квадрат <= b
end = math.floor(math.sqrt(b))

# Проходим по всем целым корням и выводим их квадраты
for i in range(start, end + 1):
    print(i*i, end=' ')
    