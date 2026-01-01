def maximalProductOperations():
    s = input().strip()
    
    # Find the minimum character in the string
    min_char = min(s)
    
    # Count operations needed - remove all characters that are not the minimum
    operations = 0
    for char in s:
        if char != min_char:
            operations += 1
    
    return operations

# Test with the examples
if __name__ == "__main__":
    result = maximalProductOperations()
    print(result)