def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Test the binary_search function
print(binary_search([1, 2, 3, 5, 8], 6))  # False
print(binary_search([1, 2, 3, 5, 8], 5))  # True
False
True
 