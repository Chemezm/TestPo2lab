import lib
import pytest

class TestFibonacci:

    # Позитивный тест с корректными данными. Возвращает последовательность Фибоначчи
    def test_positive_fibonacci(self):
        assert lib.fibonacci(5).tolist() == [0, 1, 1, 2, 3]

    # Негативный тест с n <= 0. Если мы подаем на вход n <= 0, то программа с последовательностью Фибоначчи выдает ошибку
    # Вызывается исключение ValueError
    def test_negative_fibonacci(self):
        with pytest.raises(ValueError):
            lib.fibonacci(0)

class TestBubbleSort:

    # Позитивный тест с корректными данными. Возвращает отсортированный массив
    def test_positive_bubble_sort(self):
        assert lib.bubble_sort([1, 9, 5, 3]) == [1, 3, 5, 9]

    # Негативный тест с пустым массивом. Вызывается исключение ValueErrorм
    def test_negative_bubble_sort(self):
        with pytest.raises(ValueError):
            lib.bubble_sort([])

class TestEratosthenes:

    # Функция возвращает данные для выполнения теста - корректное вычисление

    def test_sieve_valid_input(self):
        """
        Тесты для корректных входных данных.
        """
        assert lib.sieve_of_eratosthenes(10) == [2, 3, 5, 7]
        assert lib.sieve_of_eratosthenes(2) == [2]
        assert lib.sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_sieve_edge_cases(self):
        """
        Тесты для граничных значений.
        """
        assert lib.sieve_of_eratosthenes(2) == [2]
        assert lib.sieve_of_eratosthenes(3) == [2, 3]
        assert lib.sieve_of_eratosthenes(4) == [2, 3]

    def test_sieve_invalid_input(self):
        """
        Тесты для некорректных входных данных.
        """
        with pytest.raises(ValueError):
            lib.sieve_of_eratosthenes(1)  # Меньше минимально допустимого значения
        with pytest.raises(ValueError):
            lib.sieve_of_eratosthenes(0)  # Граничное значение ниже диапазона
        with pytest.raises(ValueError):
            lib.sieve_of_eratosthenes(-10)  # Отрицательное число

        with pytest.raises(TypeError):
            lib.sieve_of_eratosthenes(10.5)  # Невалидный тип данных
        with pytest.raises(TypeError):
            lib.sieve_of_eratosthenes("10")  # Невалидный тип данных