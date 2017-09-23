# coding: utf-8
"""
Script of server.
On start server waiting path to file and port, entered through a space, ex.: ..\freq_dictionary.txt 50007.
Next time alert about new user connections.
"""

from socket import *
import string
import datrie
import pickle

from auto_complete import top, match


def main():
    """For tests"""
    PATH, myPort = input().split()
    freq_dict = load_freq_dictionary(PATH)
    while True:
        connection, address = init_server('', myPort)
        print('Server connected by', address)
        while True:
            data = connection.recv(1024)
            if not data:
                break

            sequence = pickle.loads(data).split()[1]
            result = get_autocomplete(sequence, freq_dict)

            connection.send(pickle.dumps(result))  # until eof when socket closed
        connection.close()


def init_server(host, port):
    """Start server"""
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.bind((host, int(port)))
    sockobj.listen(5)
    connection, address = sockobj.accept()
    return connection, address


def load_freq_dictionary(path):
    """Load dictionary of freq from file"""
    with open(path, 'r', encoding='utf-8') as infile:
        dict_of_freq = datrie.Trie(string.ascii_lowercase)
        for line in infile:
            word, freq = line.split(' ')
            dict_of_freq[word] = int(freq)

    return dict_of_freq


def get_autocomplete(sequence, freq_dict):
    """The most frequently used words, in descending order of frequency in string"""
    match_words = match(sequence, freq_dict)
    if len(match_words) > 0:
        top_of_freq = top(match_words, 10)
        words = [word for word, freq in top_of_freq]
        result = '\n'.join(words)
        return result
    else:
        return None


if __name__ == "__main__":
    main()
