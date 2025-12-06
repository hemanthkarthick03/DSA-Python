"""
LONGEST COMMON PREFIX - Easy
Find longest common prefix string amongst array of strings.

Example: ["flower","flow","flight"] → Output: "fl"

Logical Thinking:
1. Compare characters at same position across all strings
2. Stop when mismatch found or end of any string
3. Alternative: Sort and compare first and last string

Key: Vertical scanning or sorting
Time: O(S) where S is sum of all chars | Space: O(1)
"""

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    return strs[0]

# Test cases
if __name__ == "__main__":
    print(f"Testing Longest Common Prefix...")
    print("Add your test cases here")
    print("✅ Refer to problem description for examples")
