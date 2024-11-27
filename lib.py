import numpy as np

# Функция определения чисел Фибоначчи
# Принимает n чисел
# Возвращает список последовательности Фибоначчи = n
# Пример: n = 10 => [0 1 1 2 3 5 8 13 21 34]
def fibonacci(n):
    if n <= 0:
        raise ValueError("need n > 0")
    fib_arr = np.zeros(n)
    fib_arr[1] = 1
    for i in range(2, n):
        fib_arr[i] = fib_arr[i - 2] + fib_arr[i - 1]
    return fib_arr

# Функция сортировки массива Пузырьком
# Принимает массив чисел
# Возвращает отсортированный массив
# Пример: [3 2 1 2] => [1 2 2 3]
def bubble_sort(array):
    if len(array) <= 0:
        raise ValueError("Null array")
    if len(array) <= 0:
        raise
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

"""
    param n: Целое число, до которого требуется найти все простые числа (включительно).
    return: Список простых чисел от 2 до n.
"""
def sieve_of_eratosthenes(n):

    if not isinstance(n, int):
        raise TypeError("Параметр n должен быть целым числом.")
    if n < 2:
        raise ValueError("Параметр n должен быть больше или равен 2.")

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 и 1 не являются простыми числами

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i, is_prime in enumerate(sieve) if is_prime]