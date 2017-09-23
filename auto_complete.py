# coding: utf-8
"""
Script aucomplete.
Need external library 'datrie'.
"""

from collections import Counter
import string
import datrie


def main():
    """For tests"""
    dict_of_freq, test_set = get_data()
    result = autocomplete(dict_of_freq, test_set)

    for top_10 in result:
        for word, freq in top_10:
            print(word)
        print()


def get_data():
    """Get data from input stream and create need structure"""
    n = int(input())
    dict_of_freq = datrie.Trie(string.ascii_lowercase)
    for _ in range(n):
        word, freq = input().split(' ')
        dict_of_freq[word] = int(freq)

    m = int(input())
    test_set = tuple(input() for _ in range(m))

    return dict_of_freq, test_set


def top(dictionary, n):
    """Create sorted counter dict and get top of him"""
    sorted_dict = Counter(dictionary)
    top_of_n = sorted_dict.most_common(n)

    return top_of_n


def match(sequence, dictionary):
    """Find sequence in words of dictionary"""
    match_words = dictionary.items(sequence)

    return dict(match_words)


def autocomplete(dict_of_freq, test_set):
    """The most frequently used words, in descending order of frequency"""
    result = []
    for sequence in test_set:
        match_words = match(sequence, dict_of_freq)
        top_of_freq = top(match_words, 10)
        result.append(top_of_freq)

    return result


if __name__ == "__main__":
    main()
