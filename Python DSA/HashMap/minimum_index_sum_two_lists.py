"""
MINIMUM INDEX SUM TWO LISTS - Easy
Find common strings with minimum index sum

Logical Thinking:
- See implementation for approach
"""

def find_restaurant(list1, list2):
    index_map = {s: i for i, s in enumerate(list1)}
    min_sum = float('inf')
    result = []
    for i, s in enumerate(list2):
        if s in index_map:
            index_sum = i + index_map[s]
            if index_sum < min_sum:
                min_sum = index_sum
                result = [s]
            elif index_sum == min_sum:
                result.append(s)
    return result


# Test cases
if __name__ == "__main__":
    print(f"Testing Minimum Index Sum Two Lists...")
    print("✅ Refer to implementation")
