def add_words(s1, s2):
    words1 = s1.split()
    words2 = s2.split()
    diff = len(words2) - len(words1)
    return s1 + ' ' + ' '.join(words2[-diff:])

s1 = "Hello world"
s2 = "This is a test string with many words"
print(add_words(s1, s2))
