import sys

def smallestString(N, A):
    """
    Find the lexicographically smallest string by choosing exactly one character from each string.
    
    Args:
        N (int): Number of strings in array A
        A (list): Array of strings
    
    Returns:
        str: Lexicographically smallest string possible
    """
    # Edge case: Empty input
    if N == 0 or not A:
        return ""
    
    # Edge case: Any string is empty
    for string in A:
        if not string:
            return ""
    
    result = []
    
    # For each string, find the smallest character
    for string in A:
        if string:  # Additional safety check
            min_char = min(string)
            result.append(min_char)
    
    return ''.join(result)


def main():
    N = int(sys.stdin.readline().strip())
    
    A = []
    for _ in range(N):
        A.append(sys.stdin.readline().strip())
    
    result = smallestString(N, A)
    print(result)


if __name__ == "__main__":
    main()