import sys
from collections import deque

def solve(N, X, A):
    target = int(X)
    
    # Edge case: target is 0, no operations needed
    if target == 0:
        return 0
    
    # Edge case: if target is already in array, need 1 operation
    if target in A:
        return 1
    
    # Use BFS approach but track possible sums instead of full arrays
    # Key insight: after k operations, each element becomes original + sum_of_picked_elements
    # So we need to find minimum operations where target = A[i] + sum_of_operations
    
    queue = deque()
    visited = set()
    
    # Maximum reasonable sum to avoid infinite loops
    max_sum = max(target * 2, 100000)
    min_sum = min(-target, -100000)
    
    # Queue stores (current_sum_of_operations, operations_count)
    queue.append((0, 0))
    visited.add(0)
    
    while queue:
        current_sum, ops = queue.popleft()
        
        # Check if target can be reached with current sum
        for original_val in A:
            if original_val + current_sum == target:
                return ops
        
        # Try adding each element from array A
        for num in A:
            new_sum = current_sum + num
            
            # If this sum hasn't been visited and is within reasonable bounds
            if new_sum not in visited and min_sum <= new_sum <= max_sum:
                visited.add(new_sum)
                queue.append((new_sum, ops + 1))
    
    # If we can't reach the target
    return -1

def main():
    N = int(sys.stdin.readline().strip())
    X = sys.stdin.readline().strip('\n')
    A = []
    for _ in range(N):
        A.append(int(sys.stdin.readline().strip()))
    
    result = solve(N, X, A)
    print(result)

if __name__ == "__main__":
    main()
# Te
st the solution with provided examples
def test_solution():
    print("Testing solution...")
    
    # Test case 1: N=3, X=9, A=[1,2,3]
    # Expected output: 2
    result1 = solve(3, "9", [1, 2, 3])
    print(f"Test 1: Expected 2, Got {result1}")
    
    # Test case 2: N=4, X=7, A=[2,11,6,55]  
    # Expected output: -1
    result2 = solve(4, "7", [2, 11, 6, 55])
    print(f"Test 2: Expected -1, Got {result2}")
    
    # Test case 3: N=9, X=936302870394, A=[243,42]
    # Expected output: 33
    result3 = solve(2, "936302870394", [243, 42])
    print(f"Test 3: Expected 33, Got {result3}")

if __name__ == "__main__":
    # Uncomment to run tests
    # test_solution()
    main()