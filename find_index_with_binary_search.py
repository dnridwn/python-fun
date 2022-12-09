import math

def find_index_with_binary_search(number, numbers):
    if not isinstance(numbers, list):
        return "Invalid list of numbers"
    
    first_index = 0
    mid_index = len(numbers) // 2
    last_index = len(numbers) - 1
    
    if number < numbers[first_index] or number > numbers[last_index]:
        return "Number out of range"
    
    while number != numbers[mid_index]:
        if number <= numbers[mid_index]:
            last_index = mid_index
        elif number >= numbers[mid_index]:
            first_index = mid_index
            
        mid_index = (math.ceil((last_index - first_index) / 2)) + first_index
            
    return mid_index
