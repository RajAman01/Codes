# Given a text string and a sample string.
# Find if the characters of the sample string
# is in the same order in the text string.
def FindString(string, word):
    i = 0
    words = ""
    for k in range(len(string)):
        if word[i] == string[k]:
            words += string[k]
            i += 1

    if words == word:
        print("Found")
    else:
        print("Not Found")
    print(words)


string = "abcNjhgAhGjhfhAljhRkhgRbhjbevfhO"
word = "NAGARRO"
FindString(string, word)
