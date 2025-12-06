"""
WORD LADDER - Hard
Find length of shortest transformation sequence from begin to end word.

Logical Thinking:
1. BFS with word transformations
2. For each word, try changing each character
3. Track visited words

Logical Thinking:
from collections import deque
def ladder_length(begin_word, end_word, word_list):
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    queue = deque([(begin_word, 1)])
    while queue:
        word, length = queue.popleft()
        if word == end_word:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, length + 1))
    return 0
"""

# TODO: Implement solution


# Test cases
if __name__ == "__main__":
    print(f"Testing Word Ladder...")
    print("Add your test cases here")
