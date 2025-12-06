"""
GROUP ANAGRAMS - Medium
Group anagrams together from array of strings.

Example: ["eat","tea","tan","ate","nat","bat"] → [["bat"],["nat","tan"],["ate","eat","tea"]]

Logical Thinking:
1. Anagrams have same sorted characters
2. Use sorted string as key in hashmap
3. Group strings with same key
4. Alternative: Count character frequency as key

Key: Sorting or counting, hashmap grouping
Time: O(n * k log k) | Space: O(n * k)
"""

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())


# Test cases
if __name__ == "__main__":
    print(f"Testing Group Anagrams...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
