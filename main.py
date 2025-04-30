import nltk
from nltk.corpus import brown
import string
import random
from collections import defaultdict

nltk.download('brown')
nltk.download('punkt')

def preprocess_corpus():
    sentences = brown.sents()
    preprocessed = []
    vocab = set()

    for sent in sentences:
        processed_sent = []
        for token in sent:
            token = token.lower()
            token = ''.join([c for c in token if c not in string.punctuation])
            if token:
                processed_sent.append(token)
                vocab.add(token)
        if processed_sent:
            preprocessed.append(processed_sent)
    
    return preprocessed, list(vocab)

def build_ngram(preprocessed_sentences, n):
    ngram_counts = defaultdict(int)
    for sent in preprocessed_sentences:
        if len(sent) < n:
            continue
        for gram in nltk.ngrams(sent, n):
            ngram_counts[gram] += 1
    
    return ngram_counts


def Sentence_Generator(M, N, maxLen, ngram_counts, vocab):
    possible_words = [gram[:-1] for gram in ngram_counts.keys() if len(gram) == N]
    if not possible_words:
        possible_words = [tuple([random.choice(vocab) for _ in range(N-1)])] if N > 1 else []

    sentences = []
    for _ in range(M):
        if not possible_words:
            context = tuple([random.choice(vocab) for _ in range(N-1)])
        else:
            context = random.choice(possible_words)
        

        sentence = list(context)
        current_len = len(context)

        while current_len < maxLen:
            count_of_word = sum(
                count for gram, count in ngram_counts.items()
                if gram[:-1] == context and len(gram) == N
            )

            max_prob = -1
            highest_probability_found = []

            for word in vocab:
                n_gram = tuple(list(context) + [word])
                numerator = ngram_counts.get(n_gram, 0)
                prob = numerator / count_of_word if count_of_word != 0 else 0.0

                if prob > max_prob:
                    max_prob = prob
                    highest_probability_found = [word]
                elif prob == max_prob:
                    highest_probability_found.append(word)

            if max_prob <= 0:
                next_word = random.choice(vocab)
            else:
                next_word = random.choice(highest_probability_found)


            sentence.append(next_word)
            current_len += 1

            if N == 2:
                context = (next_word,)
            else:
                context = tuple(list(context[1:]) + [next_word])

        sentences.append(' '.join(sentence[:maxLen]))

    return sentences

def main():
    M = int(input("Enter M: "))
    N = int(input("Enter N: "))
    maxLen = int(input("Enter maxLen: "))

    preprocessed_sentences, vocab = preprocess_corpus()
    if not preprocessed_sentences or not vocab:
        print("No sentences or vocab found")
        return
    
    ngram_counts = build_ngram(preprocessed_sentences, N)
    if not ngram_counts:
        print("No n-grams found")
        return
    
    sentences = Sentence_Generator(M, N, maxLen, ngram_counts, vocab)

    for sent in sentences:
        print(sent)

if __name__ == "__main__":
    main()