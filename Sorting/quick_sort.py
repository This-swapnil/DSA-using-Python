def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        lesser = [x for x in lst[1:] if x <= pivot]
        greter = [x for x in lst[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greter)


lst = [32, 454, 543, 87, 45, 988, 544, 333, 5, 0]
print(quick_sort(lst))
