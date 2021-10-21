# Leemos el índice desde memoria secundaria
index = open('../index/inverted_index.txt', 'r')
dic = {}

while True:
    line = index.readline()
    if not line:
        break
    line = line.strip()
    dict_key = line.split(":")
    books = dict_key[1].split(",")
    dic[dict_key[0]] = books

def L(query):
    return dic[query]

def AND(l1 : list , l2: list ):
    size_1 = len(l1)
    size_2 = len(l2)
    res = []
    i, j = 0, 0
    
    # Merge lineal
    while i < size_1 and j < size_2:
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            res.append(l2[j])
            i += 1
            j += 1
    return res

def AND_NOT(l1 : list , l2: list ):
    size_1 = len(l1)
    size_2 = len(l2)
    res = []
    i, j = 0, 0
    
    # Merge lineal
    while i < size_1:
        if j == size_2:
            return  res + l1[i:]
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            j += 1
        else:
            i += 1
            j += 1
    return res

def OR(l1 : list , l2: list ):
    size_1 = len(l1)
    size_2 = len(l2)
    res = []
    i, j = 0, 0

    # Merge lineal
    while i < size_1:
        if j == size_2:
            return res + l1[i:]
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            res.append(l2[j])
            j += 1
        else:
            res.append(l1[i])
            i += 1
            j += 1
    return res + l2[j:]

# Testeamos algunas raíces
f1 = "lleg"
f2 = "logr"
f3 = "irse"
f4 = "tirith"
f5 = "parth"
print(f1 + ": ", L(f1))
print(f2 + ": ", L(f2))
print(f3 + ": ", L(f3))
print(f4 + ": ", L(f4))
print(f5 + ": ", L(f5))

print()
print("(" + f1 + " AND " +  f2 + ")" + " AND NOT " + f3) #(lleg AND logr) AND NOT irse:
print(AND_NOT(AND(L(f1),L(f2)),L(f3)))

print("(" + f3 + " OR " +  f4 + ")" + " AND " + f2)     #(irse OR tirith) AND logr:
print(AND(OR(L(f3),L(f4)),L(f2)))

print("(" + f5 + " OR " + f3  + ")" +" AND " + "(" + f3 + " OR " + f2 + ")") #"(parth OR lleg) AND (irse OR logr) : "
print(AND(OR(L(f5),L(f3)),OR(L(f3),L(f2))))

index.close()