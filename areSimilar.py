def areSimilar(a, b):
    if a==b:
        return True
    if len(a) != len(b):
        return False

    dif = []
    for i in range(len(a)):
        if (a[i] != b[i]):
            dif.append(i)
    
    if len(dif) == 2:
        if (a[dif[0]] == b[dif[1]]) and (a[dif[1]] == b[dif[0]]):
            return True
    return False

a = [1, 2, 3]
b = [1, 2, 3]
print(areSimilar(a,b))
b = [2, 1, 3]
print(areSimilar(a,b))
b = [2, 1, 1]
print(areSimilar(a,b))
