# Напишите небольшую программу, которая реализует ввод
# произвольного количества чисел через пробел и выводит эти же самые числа построчно.

# Пример:
# входные данные:
# 1 2 3 4 5 6 7
# вывод:
# 1
# 2
# 3
# 4
# 5
# 6
# 7

# Примечание для продвинутых программистов:
# попробуйте решить задачу без использования циклов.

# мое решение
numbers = str(input('input:'))
for r in numbers.split():
   for t in r:
       print(t,)

# решение на сайте
numbers = input("input:")
numbers_split = numbers.split()
numbers_lines = "\n".join(numbers_split)
print(numbers_lines)