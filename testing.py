import pytest 
import fun as f

def test_pos_int_diff():
    assert f.fun(2, 1, 2, 1) == 1

def test_negative_number():
    assert f.fun(2, -2, 2, 0) == 1

def test_zero():
    with pytest.raises(ZeroDivisionError) as er:
        assert f.fun(2,2,2,2) in str(er.value)

def test_posotive_number():
    assert f.fun(0.2, -0.1, 0.2, -0.1) == 1.8257

def test_negative_root():
    assert f.fun(-2, 1, 1, 1) == "can't divide zero without complex"

def test_error_input():
    assert f.fun("asdsa", 0,0,0) == "this is not a number"
    assert f.fun("", 0,0,0) == "this is not a number"
    assert f.fun("10**-9", 0,0,0) == "this is not a number"


'Изначально проверяем деление на ноль - возникает ошибка "Деление на ноль невозможно"/пример значений (2,2,2,2) - ошибка исправлена'
'Далее проверяем отрицательное число под корнем - возникает ошибка "Под корнем не может быть отрицательное число"/пример значений (-2, 1, 1, 1) - ошибка исправлена'
'Далее рабочее выполнение программы (2, 1, 2, 1) == 1 - работает верно'
'Далее введем не число - возникает ошибка "Необхоодимо чило"/ пример ввода ("asdsa", 0,0,0) - ошибка исправлена '
'Далее проверим работу с дробными числами (0.2, -0.1, 0.2, -0.1) == 1.8257 - работает верно'
'Далее проверим что будет если ввести всего 3 значения - возникает ошибка/пример ввода ("", 0,0,0) - ошибка исправлена '
