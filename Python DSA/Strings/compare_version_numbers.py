"""
COMPARE VERSION NUMBERS - Medium
Compare two version strings

Logical Thinking:
- See implementation for approach
"""

def compare_version(v1, v2):
    parts1 = [int(x) for x in v1.split('.')]
    parts2 = [int(x) for x in v2.split('.')]
    max_len = max(len(parts1), len(parts2))
    parts1 += [0] * (max_len - len(parts1))
    parts2 += [0] * (max_len - len(parts2))
    for a, b in zip(parts1, parts2):
        if a > b:
            return 1
        elif a < b:
            return -1
    return 0


# Test cases
if __name__ == "__main__":
    print(f"Testing Compare Version Numbers...")
    print("✅ Refer to implementation")
