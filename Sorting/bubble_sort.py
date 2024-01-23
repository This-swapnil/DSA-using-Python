def bubble_sort(data_list):
    for i in range(1, len(data_list)):
        for j in range(len(data_list) - i):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]


lst = [32, 454, 543, 87, 45, 988, 544, 333, 5, 0]
bubble_sort(lst)
print(lst)
