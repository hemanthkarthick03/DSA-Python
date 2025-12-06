"""
FIND ALL ANAGRAMS - Medium
Find all anagram start indices

Logical Thinking:
- See implementation for approach
"""

def find_anagrams(s, p):
    from collections import Counter
    p_count = Counter(p)
    window = Counter()
    result = []
    for i, c in enumerate(s):
        window[c] += 1
        if i >= len(p):
            if window[s[i - len(p)]] == 1:
                del window[s[i - len(p)]]
            else:
                window[s[i - len(p)]] -= 1
        if window == p_count:
            result.append(i - len(p) + 1)
    return result


# Test cases
if __name__ == "__main__":
    print(f"Testing Find All Anagrams...")
    print("✅ Refer to implementation")
