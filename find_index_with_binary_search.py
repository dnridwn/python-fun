import math

def find_index_with_binary_search(numberToFind, numbers):
    if not isinstance(numbers, list):
        return "Invalid list of numbers"
    
    first_index = 0
    mid_index = len(numbers) // 2
    last_index = len(numbers) - 1
    
    if numberToFind < numbers[first_index] or numberToFind > numbers[last_index]:
        return "Number out of range"
    
    while numberToFind != numbers[mid_index]:
        if numberToFind <= numbers[mid_index]:
            last_index = mid_index
        elif numberToFind >= numbers[mid_index]:
            first_index = mid_index
            
        mid_index = (math.ceil((last_index - first_index) / 2)) + first_index
            
    return mid_index
