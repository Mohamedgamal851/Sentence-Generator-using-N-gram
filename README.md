# Sentence-Generator-using-N-gram
This is a python program to build a sentence generator program using bi-gram and tri-gram model.

## Requirements
Write a python program to build a sentence generator program using bi-gram and tri-gram model.
You will generate M sentences by starting with random (n-1) gram from then model and then based
on the vocabulary word with highest probability select the next word until reaching a max length
of sentence. The corpus used in this assignment is Brown Corpus in NLTK library. Get all
sentences from brown corpus. Submit your code .py or .ipynb
## Input:
• M → Number of sentences to be generated
• N → 2 for bigram, 3 for trigram
• maxLen → Max number of words in sentence generated. Used as stopping condition in
generating a sentence.
## Output:
• M sentences, each sentence contains maxLen words.

### Steps:
#### 1. Apply data preprocessing:
a. Tokenize sentences into words (Word Tokenization).
b. Remove punctuation marks from tokens.

c. Convert all tokens to lowercase.
d. Build a set of vocabulary from the pre-processed corpus.
#### 2. Build N-gram model:
Build n-gram dictionary from the corpus, where each key is a tuple of n-words (n-gram)
and the values are count of the corresponding n-gram.
#### 3. Sentence Generator:
Sentence generation process starts with a random n-1 gram from the model. Calculate the
n-gram probability for each word in the vocabulary. Then, select the next word to be the
one with highest probability. Finally, repeat selecting next word based on highest n-gram
probability until reaching maxLen.

Bigram Probability − P(wi
|wi−1) =

count(wi−1, wi)
count(wi−1)

Trigram Probability − P(wi

|wi−2, wi−1) =

count(wi−2, wi−1, wi)
count(wi−2, wi−1)
