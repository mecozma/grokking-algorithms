def binary_search(numbers, item):
    """ It returns the index of x in a given array.
    Args:
        numbers: type array.
        item: type integer.
    Returns:
        An integer.
    """
    if len(numbers) == 0:
        return "Please provide an array"

    start = 0
    end = len(numbers) - 1

    while start <= end:
      middle = (start + end) // 2
      guess = numbers[middle]
      # Checks if the item is pressent at mid.
      if item == guess:
        return middle
      # If item is greater, ignore left half.
      elif item > guess:
        start = middle + 1
      # If item is smaller, ignore right half.
      else:
        end = middle - 1
    return None

# Test list.
numbers_array = [1, 2, 3, 4, 5, 7, 8, 9, 10]

# Number to identify.
wally = 4

# Function call
result = binary_search(numbers_array, wally)

if result == None:
    print("Number is not present in the array")
else:
    print(f"The element is present at index: {result}")
