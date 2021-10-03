def CountFreq(str):
    str = str.split()
    str2 = []
    for i in str:
        if i not in str2:
            str2.append(i)
    for i in range(0, len(str2)):
        print("The Frequency of Word",str2[i],"", str.count(str2[i]))


str = 'apple mango apple orange orange apple guava mango mango'
CountFreq(str)
