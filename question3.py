import string

def word_frequency(sentence):
    # Initialize a dictionary to store word frequencies
    word_freq = {}

    # Remove punctuation from the sentence and split it into words
    words = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split()

    # Count the frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)