def find_smallest(arr):
    """Finds the smalles number in a list."""
    smallest_number = arr[0]
    smallest_number_index = 0
    # Iterate through the list. 
    for i in range(1, len(arr)):
        if arr[i] < smallest_number:
            smallest_number = arr[i]
            smallest_number_index = i
    return smallest_number_index


def selection_sort(arr):
    """Sorts a list."""
    new_list = []
    # Iterates through the list.
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_list.append(arr.pop(smallest))
    return new_list


random_list = [9, 8, 3, 2, 7] 
sorted_list = selection_sort(random_list)
if len(random_list) == 0 and random_list == None:
    print("Please provide an array!")
else:
    print(f"Sorted list: {sorted_list}")
