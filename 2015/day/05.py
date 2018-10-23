def isNice1(str):
    if sum([str.count(i) for i in 'aeiou']) < 3 \
            or sum([1 for i in range(1,len(str)) \
            if str[i] == str[i-1]]) < 1 \
            or sum([1 for i in ['ab', 'cd', 'pq', 'xy'] \
            if i in str]) > 0:
        return False
    return True

def isNice2(str):
    if sum([1 for i in range(len(str)-3) \
            for j in range(i+2, len(str)-1) \
            if str[i]+str[i+1] == str[j]+str[j+1]]) < 1 \
            or sum([1 for i in range(len(str)-2) \
            if str[i] == str[i+2]]) < 1:
        return False
    return True

with open("../input/05.txt") as f:
    input = f.read().strip().splitlines()

print(sum([1 for i in input if isNice1(i)]))
print(sum([1 for i in input if isNice2(i)]))

