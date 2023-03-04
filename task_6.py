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


