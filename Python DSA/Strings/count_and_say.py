"""
COUNT AND SAY - Medium
Generate nth term of count-and-say

Logical Thinking:
- See implementation for approach
"""

def count_and_say(n):
    result = '1'
    for _ in range(n - 1):
        next_result = []
        i = 0
        while i < len(result):
            count = 1
            while i + 1 < len(result) and result[i] == result[i + 1]:
                i += 1
                count += 1
            next_result.append(str(count) + result[i])
            i += 1
        result = ''.join(next_result)
    return result


# Test cases
if __name__ == "__main__":
    print(f"Testing Count And Say...")
    print("✅ Refer to implementation")
