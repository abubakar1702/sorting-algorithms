def insertionSort(my_list):
    for i in range(1, len(my_list)):
        current = my_list[i]
        while current < my_list[i-1] and i>0:
            my_list[i] = my_list[i-1]
            i = i- 1
        my_list[i] = current

my_list = [2,4,3,5,1]

insertionSort(my_list)
print(my_list)