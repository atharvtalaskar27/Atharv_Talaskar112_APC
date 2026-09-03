# 4. Create a package texttools containing:
# a) cleaning.py – remove punctuation and extra spaces
# b) tokenization.py – tokenize text
# c) frequency.py – word-frequency analysis
# Create a main program to use the package.


from texttools.cleaning import remove_punctuation, remove_extra_spaces
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency


text = input("Enter a sentence: ")


cleaned_text = remove_punctuation(text)

cleaned_text = remove_extra_spaces(cleaned_text)


print("\nCleaned Text:")
print(cleaned_text)


words = tokenize(cleaned_text)


print("\nTokens:")
print(words)


frequency = word_frequency(words)


print("\nWord Frequency:")

for word, count in frequency.items():
    print(word, ":", count)
