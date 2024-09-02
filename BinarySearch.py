# Binary search is a more efficient algorithm than linear search, but it requires the list to be sorted.
# It works by repeatedly dividing the search interval in half and comparing the target value 
# to the middle element. If the target value is smaller, the search continues only on the left half; 
# if larger, it continues only on the right half.

def binary_search(arr, target):

    left = 0, 
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Example usage:
arr = [2, 35, 4, 71, 90, 105, 41,]
target = 105

result = binary_search(arr, target)

if result != False:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
