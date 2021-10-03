def rotateWord(str,k):
    word = str.split()
    for i in range(0,k):
        for j in range(0,len(word)):
            word[j] = word[j][1:]+word[j][0]
    count = 0
    for k in range(0,len(word)):
        if  word[k] in str:
            count+=1
    print(count)
rotateWord("adaada", 3)
rotateWord("loHel endFri", 3)
rotateWord("Hello dFrien", 5)