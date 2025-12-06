"""
DAILY TEMPERATURES - Medium
Return array where answer[i] is days until warmer temperature.

Logical Thinking:
1. Use stack to store indices
2. For each temperature, pop stack while current is warmer
3. Calculate difference in indices

Logical Thinking:
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)
    return result
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Daily Temperatures...")
    print("Add your test cases here")
