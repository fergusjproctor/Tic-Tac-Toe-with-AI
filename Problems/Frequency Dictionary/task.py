# put your python code here
inp = input().lower().split()
counts = dict()
for word in inp:
    if word in counts.keys():
        counts[word] += 1
    else:
        counts[word] = 1

for key, value in counts.items():
    print(key + ' ' + str(value))

