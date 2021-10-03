s = "i like this program very much"

words = s.split(' ')
strings = []
for i in words:
    strings.insert(0,i)
print(" ".join(strings))

