lst = [1,2,3,4,5]

def split(lst, n):
    return [lst[i::n] for i in range(n)] # В каждой итерации создается подсписок, начиная с i-го элемента и берущего каждый n-ный элемент далее.

print(split(lst, 2))
print(split(lst, 3))