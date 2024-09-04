# Begin with the second element in the array. Compare the current element with the elements before it. 
# Insert the current element into its correct position in the sorted portion.
# Move to the next element in the list and repeat the process until all elements are sorted.

def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = [12, 51, 13, 75, 62, 22]
print("Original array:", arr)

insertion_sort(arr)
print("Sorted array:", arr)
