# =====================================================================================================
# Basic coding problems on Python Strings and various data types (list, set, tuples and dict) concepts
# =====================================================================================================

# ------------------------------------------------
# 1. Reverse Every Word
# ------------------------------------------------
# Problem: Reverse each word in a sentence but keep the word order.
# Example: "Hello world from Python" -> "olleH dlrow morf nohtyP"

sentence = "Hello world from Python"
reversed_words = ' '.join(word[::-1] for word in sentence.split())
print(reversed_words)
# Output: olleH dlrow morf nohtyP
# Explanation: The string is split into words, each reversed via slicing [::-1], then joined back with spaces.

# ------------------------------------------------
# 2. Count Vowels and Consonants
# ------------------------------------------------
# Problem: Count vowels and consonants in a given string.

text = "Hello, World!"
vowels = 'aeiou'
vowel_count = sum(1 for ch in text.lower() if ch in vowels)
consonant_count = sum(1 for ch in text.lower() if ch.isalpha() and ch not in vowels)
print("Vowels:", vowel_count, "Consonants:", consonant_count)
# Output: Vowels: 3 Consonants: 7
# Iterate through each character, checking membership in vowel list.

# ------------------------------------------------
# 3. Palindrome Checker (Ignoring Spaces & Case)
# ------------------------------------------------
phrase = "A man a plan a canal Panama"
cleaned = ''.join(ch.lower() for ch in phrase if ch.isalnum())
is_palindrome = cleaned == cleaned[::-1]
print(is_palindrome)
# Output: True
# Cleaned string removes spaces/punctuation, then checks if reversed equals itself.

# ------------------------------------------------
# 4. Substring Frequency Map (length 3)
# ------------------------------------------------
text = "abababab"
sub_len = 3
counts = {}
for i in range(len(text) - sub_len + 1):
    sub = text[i:i+sub_len]
    counts[sub] = counts.get(sub, 0) + 1
print(counts)
# Output: {'aba': 3, 'bab': 3}
# Loops through all substrings of length 3 and counts frequency using a dictionary.

# ------------------------------------------------
# 5. Clean and Title-Case a Sentence
# ------------------------------------------------
raw = "   hELLo   worLD  Python!!  "
cleaned = ' '.join(raw.split())  # remove extra spaces
title_case = cleaned.title().strip('!')
if not title_case.endswith('.'):
    title_case += '.'
print(title_case)
# Output: Hello World Python.
# Removes extra spaces, capitalizes words, ensures sentence ends with a period.

# ------------------------------------------------
# 6. Longest Word in a Sentence
# ------------------------------------------------
sentence = "The quick brown fox jumped over the lazy dog"
words = sentence.split()
longest = max(words, key=len)
print(longest, len(longest))
# Output: jumped 6
# split() makes words list; max() finds the longest by length.

# ------------------------------------------------
# 7. Replace Words Using Mapping
# ------------------------------------------------
text = "I love Python code."
mapping = {'python': 'snake', 'code': 'program'}
words = text.split()
new_words = [mapping.get(w.lower().strip('.'), w) for w in words]
result = ' '.join(new_words)
print(result)
# Output: I love snake program
# Replace matching words via dictionary, keeping non‑mapped words unchanged.
