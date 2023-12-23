lst = [1,2,3,4,5]

def split(lst, n):
    if len(lst) <= 1: # Проверяем, пуст ли список
        return []
    else:
        if len(lst) < n:  
            n = len(lst)
        return [lst[i::n] for i in range(n)]

print(split(lst, 2))
print(split(lst, 3))
print(split([], 2))
print(split([], 3))
print(split([2, 1], 4))