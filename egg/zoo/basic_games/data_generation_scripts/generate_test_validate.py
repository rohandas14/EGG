import numpy as np
import random
import sys

def gen_language(index, message_length, vocab_len):
    if index == message_length -1:
        return [[i] for i in range(vocab_len)]
    ans = []
    child = gen_language(index + 1, message_length, vocab_len)

    for lang in child:
        for vocab in range(vocab_len):
            t = lang.copy()
            t.append(vocab)
            ans.append(t)
    return ans

def data_generation(vocab_len, message_length = -1):
  # if no specific message_length is provided, it will assume vocab length
  if message_length == -1:
    message_length = vocab_len

  return gen_language(0, message_length, vocab_len)
  print(data)


def writeToFile(data, vocab_len, message_length, trainValidateRatio = 0.9, filename = "out", shuffle = True):
  train = open(filename +"_train_v=" + str(vocab_len)+"_m=" + str(message_length), "w")
  valid = open(filename +"_valid_v=" + str(vocab_len)+"_m=" + str(message_length), "w")

#   print("Data is",data)
  if shuffle:
    np.random.shuffle(data)
  
  for i in range(len(data)):
    file = train
    if i > trainValidateRatio * len(data):
      file = valid
    for j in range (len(data[i])):
      file.write(str(data[i][j]) + " ")
    file.write('\n')
  


vocab_len = int(sys.argv[1])
message_length = int(sys.argv[2])
print("Creating files for vocab = ", vocab_len, " and message length = ", message_length)

data = data_generation(vocab_len, message_length)
#
# Generates 2 files, train and valid, with vocab and message lengths
# 
writeToFile(data, vocab_len, message_length)


