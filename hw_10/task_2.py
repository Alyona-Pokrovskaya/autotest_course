# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest

def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test1():
    assert 5 / 0, 'на ноль делить нельзя'


@pytest.mark.smoke
def test2():
    assert 6 / 2 == 3


@pytest.mark.acceptence
def test3():
    assert 5 / 3 == 1, 'Неверный результат деления'


@pytest.mark.acceptence
def test4():
    assert 9.6 / 6 == 1.5999999999999999


@pytest.mark.acceptence
def test5():
    assert -10 / 5 == -2


@pytest.mark.acceptence
def test6():
    assert 6 / 'b' == 3, 'Нельзя число делить на строку'


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division
