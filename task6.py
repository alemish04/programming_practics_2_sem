def sorted_indices(lst):
    return sorted(range(len(lst)), key=lambda k: lst[k])


lst = [2, 3, 1, 5, 4]
print(sorted_indices(lst))
