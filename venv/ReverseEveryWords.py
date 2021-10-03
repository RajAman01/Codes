def reverse(str):
    word = str.split(' ')
    newWord = [words[::-1]for words in word]
    newSentance = ' '.join(newWord)
    print(newSentance)
Sentence = "GeeksforGeeks is good to learn"
reverse(Sentence) 