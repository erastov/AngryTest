# coding: utf-8
"""
Script client.
On start server waiting host and port, entered through a space, ex.: localhost 50007.
Next you can to enter query of format 'get <prefix>', ex.: get aaa.
"""

from socket import *
import pickle


def main():
    """For tests"""
    serverHost, serverPort = input().split()
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((serverHost, int(serverPort)))

    while True:
        message = pickle.dumps(input())

        sockobj.send(message)
        data = pickle.loads(sockobj.recv(1024))
        if data:
            print(data)
        else:
            print('Ничего не найдено')
        print()

    sockobj.close()

if __name__ == "__main__":
    main()
