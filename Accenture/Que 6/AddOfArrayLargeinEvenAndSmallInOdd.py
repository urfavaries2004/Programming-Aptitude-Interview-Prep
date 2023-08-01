def LargeSmallSum(arr):
    if len(arr) == 0 or len(arr) <= 3: #condition for the check the arr size is small or large
        return 0

    even_positions = [arr[i] for i in range(0, len(arr), 2)] 
    odd_positions = [arr[i] for i in range(1, len(arr), 2)]

    even_positions.sort()
    odd_positions.sort()

    return even_positions[-2] + odd_positions[1]

# Test example
arr1 = [3, 2, 1, 7, 5, 4]
result1 = LargeSmallSum(arr1)
print("Output:", result1)  # Output: 7

arr2 = [1, 8, 0, 2, 3, 5, 6]
result2 = LargeSmallSum(arr2)
print("Output:", result2)  # Output: 8
