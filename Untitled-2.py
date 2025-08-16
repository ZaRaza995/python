# пользователь вводит строку чисел
user_input = input("Введите числа через пробел: ")

# превращаем строку в список чисел
numbers = [int(x) for x in user_input.split()]

# считаем сумму, максимум, минимум, среднее
total = 0
for n in numbers:
    total += n

max_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n

min_num = numbers[0]
for n in numbers:
    if n < min_num:
        min_num = n

average = total / len(numbers)

print("Сумма:", total)
print("Максимум:", max_num)
print("Минимум:", min_num)
print("Среднее:", average)
