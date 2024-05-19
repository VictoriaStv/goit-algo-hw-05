def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0
    
    while left <= right:
        mid = (left + right) // 2
        iterations += 1
        
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return (iterations, arr[mid])
    
    if left < len(arr):
        return (iterations, arr[left])
    else:
        return (iterations, arr[right])

# Тест
arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
print(binary_search(arr, 3.5))  
print(binary_search(arr, 4)) 
print(binary_search(arr, 6.0))  
