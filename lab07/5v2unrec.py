def func(i):
    if i == 1 or i == 2:
        return 0
    elif i == 3:
        return 1.5
    else:
        prev1, prev2, prev3 = 0, 0, 1.5
        current = 0
        for j in range(4, i+1):
            current = (j+1)/((j*j)+1) * prev3 - prev2 * prev1
            prev1, prev2, prev3 = prev2, prev3, current
        return current

result = func(4)
print(result)
