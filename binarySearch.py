import math
from clean_data import remove_duplicates

def binary_search(target):
    search_array = remove_duplicates()
    left = 0
    right = len(search_array) -1
    while left < right:
        mid = math.floor((left + right)/2)
        if search_array[mid] == target:
            return mid
        elif search_array[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1

print(binary_search("Liliane Mugabo"))