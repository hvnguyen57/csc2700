import collections
import re
import itertools

# Opening the file and reading the text
with open('warandpeace.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Number of words
words = re.findall(r'\b\w+\b', text)
num_words = len(words)

# Number of vowwels
num_vowels = sum(1 for char in text if char.lower() in 'aeiouAEIOU')

# Number of distinct words
distinct_words = collections.Counter(words)
num_distinct_words = len(distinct_words)

# Number of sentences
sentences = re.split(r'[.!?]', text)
num_sentences = len(sentences)

# Number of paragraphs
paragraphs = re.split(r'\n\n+', text)
num_paragraphs = len(paragraphs)

# Letter frequencies
letter_freq = collections.Counter(text.lower())

# Word frequencies
word_freq = collections.Counter(words)

# Sentence frequencies
sentence_freq = collections.Counter(sentences)

# Pair frequencies
pair_freq_sentence = collections.Counter()
for sentence in sentences:
    sentence_words = re.findall(r'\b\w+\b', sentence)
    pair_freq_sentence.update(itertools.combinations(sentence_words, 2))

# Pair frequencies in paragraphs
pair_freq_paragraph = collections.Counter()
for paragraph in paragraphs:
    paragraph_words = re.findall(r'\b\w+\b', paragraph)
    pair_freq_paragraph.update(itertools.combinations(paragraph_words, 2))

# Printing the results
print(f'Number of words: {num_words}')
print(f'Number of vowels: {num_vowels}')
print(f'Number of distinct words: {num_distinct_words}')
print(f'Number of sentences: {num_sentences}')
print(f'Number of paragraphs: {num_paragraphs}')
print(f'Letter frequencies: {letter_freq}')
print(f'Word frequencies: {word_freq}')
print(f'Sentence frequencies: {sentence_freq}')
print(f'Pair frequencies in sentences: {pair_freq_sentence}')
print(f'Pair frequencies in paragraphs: {pair_freq_paragraph}')

# Closing the file
file.close()