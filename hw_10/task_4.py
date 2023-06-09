# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest

class Test:
    def test_one(self, test_fixture):
        assert 6 / 3 == 2

    def test_two(self, test_fixture):
        list_test = list(range(1, 10))
        assert list_test == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_three(self):
        assert 3 == 3

