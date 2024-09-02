# Linear search is an algorithm that checks each element in a list one by one
# until the target element is found or the end of the list is reached.
# Its is not the most efficient for large lists, as its time complexity is O(n).

def linear_search(arr, target):
    # Iterate through the array
    for i in range(len(arr)):
        # Check if the current element is equal to the target
        if arr[i] == target:
            return i  # Return the index of the found element
    return False  # Return -1 if the element is not found

# Example usage:
arr = [32, 51, 27, 42, 90, 107, 5, 201]
target = 42

result = linear_search(arr, target)

if result != False:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
