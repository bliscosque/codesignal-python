def addBorder(picture):
    i=len(picture[0])
    out = []
    out.append('*' * (i+2))
    for line in picture:
        out.append('*' + line + '*')
    out.append('*' * (i+2))

    return out


picture = ["abc",
           "ded"]
print(addBorder(picture))


