import re

from constants import ONE_WORD_ABREBIATION, TWO_WORDS_ABREBIATION, THREE_WORDS_ABREBIATION, \
    SENTENCE_PATTERN, WORD_PATTERN, NON_DECLARATIVE_PATTERN, NUMBER_PATTERN, DIRECT_SPEECH_PATTERN \
    

def count_sentences(text: str) -> int:
    amount = len(re.findall(SENTENCE_PATTERN, text))

    for abbreviation in ONE_WORD_ABREBIATION:
        amount -= text.lower().count(abbreviation) 

    for abbreviation in TWO_WORDS_ABREBIATION:
        amount -= text.lower().count(abbreviation) * 2

    for abbreviation in THREE_WORDS_ABREBIATION:
        amount -= text.lower().count(abbreviation) * 3      

    direct_speeches = re.findall(DIRECT_SPEECH_PATTERN, text)
    for direct_speech in direct_speeches:
        amount -= count_sentences(direct_speech)

    return amount if amount >= 0 else 0

def count_non_declarative(text: str) -> int:
    text = text + "\0"
    amount = len(re.findall(NON_DECLARATIVE_PATTERN, text))

    direct_speeches = re.findall(DIRECT_SPEECH_PATTERN, text)
    for direct_speech in direct_speeches:
        amount -= count_sentences(direct_speech)

    return amount

def calc_average_sentence_length(text: str) -> float:
    words = [word for word in re.findall(WORD_PATTERN, text) if word not in re.findall(NUMBER_PATTERN, text)]
    words_len = sum(len(word) for word in words)
    return words_len / count_sentences(text) if count_sentences(text) != 0 else 0

def calc_average_word_length(text: str) -> float:
    words = re.findall(WORD_PATTERN, text)
    words_len_in_characters = sum(len(word) for word in words)
    return words_len_in_characters / len(words) if len(words) != 0 else 0

def calc_topK_repeated_Ngrams(text: str, k: int = 10, n: int = 4) -> list:
    text = text.lower()
    text = re.sub("\n", " ", text)
    ngrams = []

    for i in range(len(text) - n + 1):
        ngrams.append(text[i:i + n])
    frequency_dictionary = count_frequency(ngrams)
    sorted_frequencies = sorted(frequency_dictionary.items(), key=lambda item: item[1], reverse=True) #список кортежей
    return sorted_frequencies[:k]

def count_frequency(elements):
    frequencies = {}
    for el in elements:
        frequencies[el] = frequencies.get(el, 0) + 1
    return frequencies