# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest

def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result', [
    (5, 0, 'На ноль делить нельзя'),
    pytest.param(6, 2, 3, marks=pytest.mark.smoke('smoke')),
    pytest.param(5, 3, 1, marks=pytest.mark.skip('bad test')),
    (9.6, 6, 1.5999999999999999),
    (-10, 2, -5)
],
                         ids=['negative1', 'positive1', 'negative2', 'positive2', 'positive3'])
def test_parameters(a, b, result):
    assert a/b == result

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division




