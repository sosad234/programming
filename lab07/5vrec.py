def split(lst, n):
    if len(lst) <= 1:  # Проверяем, пуст ли список или содержит только один элемент
        return []
    elif n > len(lst):  # Проверяем, можно ли дальше делить список
        return split(lst, len(lst))
    else:
        return [lst[i::n] for i in range(n)]

lst = [1, 2, 3, 4, 5]
print(split(lst, 2))
print(split(lst, 3))
print(split([], 2))
print(split([], 3))
print(split([2, 1], 4))
