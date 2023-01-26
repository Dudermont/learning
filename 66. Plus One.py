def plusOne(digits):
    k = []
    for i in str(int("".join(map(str, digits))) + 1):
        k.append(int(i))
    return k


print(plusOne([1, 2, 3]))
