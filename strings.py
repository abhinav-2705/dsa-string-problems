def is_palindrome(s):
    return s == s[::-1]

def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

print(is_palindrome("madam"))
print(count_vowels("hello"))
