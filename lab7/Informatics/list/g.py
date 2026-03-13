# Считываем количество элементов
n = int(input())

# Считываем массив
arr = list(map(int, input().split()))

# Разворачиваем массив на месте
for i in range(n // 2):
    arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

# Выводим результат
print(*arr)