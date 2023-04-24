def writeToSplits(vocab_len, message_length, fileName):
            
    train25 = open("out_25_train_v=" + str(vocab_len)+"_m=" + str(message_length), "w")
    train50 = open("out_50_train_v=" + str(vocab_len)+"_m=" + str(message_length), "w")
    train75 = open("out_75_train_v=" + str(vocab_len)+"_m=" + str(message_length), "w")
   
    f = open(fileName, "r")
    totalLines = vocab_len ** message_length
    print("Total lines = ", totalLines)

    i = 0
    for x in f:
        if i <= 0.25*totalLines:
            train25.write(x)
            train50.write(x)
            train75.write(x)
        elif i<=0.5*totalLines:
            train50.write(x)
            train75.write(x)
        elif i<=0.75*totalLines:
            train75.write(x)
        else:
            print("All i finished at i = ", i)
            break
        i +=1



writeToSplits(4, 4, "out_train_v=4_m=4")