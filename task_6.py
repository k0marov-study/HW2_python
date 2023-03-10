"""
Для расчёта этого значения нужны факториалы 1!, 2!, 3!, 4! ... N!
Их необязательно находить каждый отдельно, ведь каждый следующий элемент этой последовательности равен его номеру умножить на предыдущий элемент. 
Засчёт этого достигается асимптотика O(n). 

Но если запустить этот алгоритм для значений >9, то оказывается, что результат
с точностью до пяти знаков не меняется. 
Это логично, учитывая что значение N! увеличивается очень быстро, 
а значит 1/N! быстро становится очень маленьким и почти не влияющим на сумму. 
Уже для N=10: 1/10! ~= .0000002, 
что никак не может повлиять на сумму с точностью до 5 знаков после запятой. 

В итоге эта функция стремится к 2.71828, что равно числу Эйлера (Бог знает, почему).
"""
n = int(input())
e = 2.71828

if n <= 9: 
    res = 1 
    current_factorial = 1 
    for i in range(1, n+1): 
        current_factorial *= i 
        res += 1/current_factorial
    print(format(res, '.5f'))
else: 
    print(e)


