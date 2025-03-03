def merge_sort(array):
    """
    Sorts an array in ascending order using the merge sort algorithm.
    Merge sort is a divide-and-conquer algorithm that splits the array into two halves,
    recursively sorts each half, and then merges the sorted halves back together.
    Parameters:
    array (list): The list of elements to be sorted.
    Returns:
    None: The function sorts the array in place and does not return a value.
    """
    if len(array) <= 1:
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1
    print('Sorted array: ' + str(array))

if __name__ == '__main__':
    numbers = [12, 7, 91, 45, 9, 18, 32, 56, 1, 78, 2, 14, 67, 89, 3, 90, 54, 11, 22, 27, 41, 61, 36, 80, 4]

    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Final sorted array: ' + str(numbers))
