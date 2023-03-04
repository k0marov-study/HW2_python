x = int(input()) 

dels_count = 0
for d in range(1, int(x**0.5) + 1): 
    if x % d == 0: 
        dels_count += 1 if x // d == d else 2 

print(dels_count)
