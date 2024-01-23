def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp


lst = [32, 454, 543, 87, 45, 988, 544, 333, 5, 0]
insertion_sort(lst)
print(lst)
