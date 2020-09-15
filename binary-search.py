def binary_search(numbers, item):
  start = 0
  end = len(numbers) - 1

  while start <= end:
    middle = (start + end) // 2
    guess = numbers[middle]
    if item == guess:
      return middle
    elif item > guess:
      start = middle + 1
    else:
      end = middle - 1
  return None
  
numbers_array = [1, 2, 3, 4, 5, 7, 8, 9, 10]

print(binary_search(numbers_array, 10))


















