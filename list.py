# Создаем ряд чисел Фибоначчи до N
N  = input() 
N  = int(N )
fib_list = [0, 1]

for i in range (0,N):

while fib_list[-1] + fib_list[-2] < N:
    fib_list.append(fib_list[-1] + fib_list[-2])
# Преобразуем числа в списке
converted_list = []
for num in fib_list:
    if num % 2 == 0:
        converted_list.append(num * 2)
    else:

        converted_list.append(num ** 2)
tf_list = converted_list
# Анализируем список
min = min(tf_list)
max = max(tf_list)
length = len(tf_list) # длина
count = len(tf_list) // 2 #медианного значения




#Вывод 
print(f"Исходный ряд Фибоначчи до {N}: {fib_list}")
print(f"Преобразованный ряд: {converted_list}")
print(f"Минимальное значение: {min}")
print(f"Максимальное значение: {max}")
print(f"Длина списка: {length}")
print(f"Количество элементов: {count}")