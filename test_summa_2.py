import summa_2


def test_summa_correct_output():
    assert summa_2.summa('5 5 5') == 'Сумма чисел равна 15.0'
    assert summa_2.summa('2 2') == 'Сумма чисел равна 4.0'
    assert summa_2.summa('2.0 -2.0') == 'Сумма чисел равна 0.0'


def test_summa_except():
    assert summa_2.summa('hello') == 'Должны быть только числа!'
    assert summa_2.summa('2 d') == 'Должны быть только числа!'
