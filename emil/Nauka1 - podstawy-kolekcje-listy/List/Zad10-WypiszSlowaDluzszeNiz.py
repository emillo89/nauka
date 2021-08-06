def long_words(n,words):
    word_length = []
    text = words.split(" ")
    for x in text:
        if len(x) > n:
            word_length.append(x)
    return word_length

print(long_words(3, "The quick brown fox jumps over the lazy dog"))


