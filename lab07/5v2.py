def func(i):
    if i == 1:
        return 0
    elif i == 2:
        return 0
    elif i == 3:
        return 1.5
    else:
        A = (i+1)/((i*i)+1) * func(i-1) - func(i-2) * func(i-3)
        print(A)
        return A

func(4)