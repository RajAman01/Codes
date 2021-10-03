lst = ["a", "b", "a", "c", "c", "a", "c"]
temp = set(lst)
result = {}
print(temp)
for i in (temp):
    result[i] = lst.count(i)
print(result)
str = "this is my book"
print(str.title())
def count(str):
    count = dict()
    words = str.split()
    for i in words:
        if i in count:
            count[i]+=1
        else:
            count[i] = 1
    return count
def check(str):
    count = {}
    for s in str:
        if s in count:
            count[s]+=1
        else:
            count[s] = 1
    for i in count:
        if count[i] == 1:
            print(i,count[i])
check(str)

str = "the quick brown fox jumps over the lazy dog."
print(count(str))