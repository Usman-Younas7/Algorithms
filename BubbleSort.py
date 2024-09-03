# Bubble sort is a sorting algorithm that repeatedly steps through the list, 
# compares adjacent elements, and swaps them if they are in the wrong order. 

def bubble_sort(arr):
    
    n = len(arr)
    swapped = True
    
    # Continue looping until no swaps are made
    while swapped:
        swapped = False
        for i in range(1, n):
            # Compare adjacent elements
            if arr[i-1] > arr[i]:
                # Swap using a temporary variable
                temp = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = temp
                swapped = True
        # Reduce n as the last element is sorted
        n -= 1
    
    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
