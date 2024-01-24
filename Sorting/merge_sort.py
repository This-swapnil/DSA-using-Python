from turtle import left


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_lst = lst[:mid]
        right_lst = lst[mid:]
        merge_sort(left_lst)
        merge_sort(right_lst)

        i, j, k = 0, 0, 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i += 1
            else:
                lst[k] = right_lst[j]
                j += 1
            k += 1
        while i < len(left_lst):
            lst[k] = left_lst[i]
            i += 1
            k += 1
        while j < len(right_lst):
            lst[k] = right_lst[j]
            j += 1
            k += 1


lst = [32, 454, 543, 87, 45, 988, 544, 333, 5, 0]
merge_sort(lst)
print(lst)
