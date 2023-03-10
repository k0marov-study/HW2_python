"""
Хорошесть прибавляют подстроки типа ab, bc, cd и тд.
Значит, если у нас 30 штук "a" и 40 штук "b", 
то мы можем получить хорошесть 30, поставив 30 ab. 
И таким же образом нужно брать bc, cd и тд. 
Получается, что ответом будет сумма минимумов от каждой пары соседних элементов.
"""


n = int(input())
res = 0
prev = 0
for _ in range(n):
    curr = int(input())
    res += min(prev, curr)
    prev = curr

print(res)
