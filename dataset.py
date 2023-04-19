import numpy as np
import random
def data_generation(vocab_len, n, message_length=-1):
    if message_length == -1:
        message_length = vocab_len

    vocab = []
    for i in range(vocab_len + 1):
        vocab.append(i)

    data = []

    for j in range(n):
        t = []
        for i in range(message_length):
            n = (int)(random.random() * vocab_len)
            t.append(n)
        data.append(t)
    return data


def writeToFile(data, trainValidateRatio=0.8, filename="out"):
    train = open(filename + "_train", "w")
    valid = open(filename + "_valid", "w")

    for i in range(len(data)):
        file = train
        if i > trainValidateRatio * len(data):
            file = valid
        for j in range(len(data[i])):
            file.write(str(data[i][j]) + " ")
        file.write('\n')


vocab_len = 2
total_messages = 100
message_length = 3

writeToFile(data_generation(vocab_len, total_messages, message_length))