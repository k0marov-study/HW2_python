"""
Сначала находим наибольший элемент первым итерированием по массиву, 
затем вторым итерированием находим количество равных ему элементов. 
"""
a = [] 

x = int(input()) 
while x != 0: 
    a.append(x) 
    x = int(input()) 

max_elem = 0 
for x in a: 
    if x > max_elem: 
        max_elem = x 

equal_max_cnt = 0 
for x in a: 
    if x == max_elem: 
        equal_max_cnt += 1

print(equal_max_cnt)
