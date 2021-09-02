lists = []
vas = []
for i in range(2):
    lists.append([])
    for j in range(1):
        lists[i].append(["aaa","bbb","ccc"])

for i in lists:
    for j in i:
        print(j[0],j[1])
print(lists)
for i in range(2):
    print(lists[i][0][0])