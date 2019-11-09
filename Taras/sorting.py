import random

a = [int(1000*random.random()) for i in range(10000)]


def bubble_sort(array):
    for i in range(len(array)):
        for n in range(len(array)-1-i):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
    return array


print(bubble_sort(a))


def quick_sort(array):
    if len(array) <= 1:
        return array
    rand_int = random.choice(array)

    greater = [num for num in array if num > rand_int]
    less = [num for num in array if num < rand_int]
    equal = [rand_int] * array.count(rand_int)

    return quick_sort(less) + equal + quick_sort(greater)


print(quick_sort(a))


def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2

    left_list = merge_sort(array[:middle])
    right_list = merge_sort(array[middle:])

    return merge(left_list, right_list)


def merge(left_list, right_list):
    sorted_list = []
    l_index, r_index = 0, 0
    for _ in range(len(left_list) + len(right_list)):
        if l_index < len(left_list) and r_index < len(right_list):
            if left_list[l_index] < right_list[r_index]:
                sorted_list.append(left_list[l_index])
                l_index += 1
            else:
                sorted_list.append(right_list[r_index])
                r_index += 1

        elif l_index == len(left_list):
            sorted_list.append(right_list[r_index])
            r_index += 1
        elif r_index == len(right_list):
            sorted_list.append(left_list[l_index])
            l_index += 1
    return sorted_list

print(merge_sort(a))

