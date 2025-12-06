"""
LONGEST REPEATING CHARACTER REPLACEMENT - Medium
Longest substring with k replacements
"""

def character_replacement(s, k):
    from collections import Counter
    count = Counter()
    max_count = left = result = 0
    for right in range(len(s)):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])
        if right - left + 1 - max_count > k:
            count[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result


if __name__ == "__main__":
    print("✅ Longest Repeating Character Replacement")
