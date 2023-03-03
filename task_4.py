best = 0 
curr = 0 

prev = None
is_increasing = None 
a = int(input()) 
while a != 0: 
    any_fits = prev is None or is_increasing is None
    if a != prev and (any_fits or (a > prev) == is_increasing): 
        is_increasing = a > prev if prev is not None else None
        curr += 1
    else: 
        is_increasing = not is_increasing if a != prev else None
        best = curr if curr > best else best 
        curr = 2 if a != prev else 1 
    prev = a 
    a = int(input())

best = curr if curr > best else best 

print(best)

