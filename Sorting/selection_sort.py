def selection_sort(data_list):
    n = len(data_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data_list[j] < data_list[min_index]:
                min_index = j
        data_list[i], data_list[min_index] = data_list[min_index], data_list[i]


lst = [32, 454, 543, 87, 45, 988, 544, 333, 5, 0]
selection_sort(lst)
print(lst)
