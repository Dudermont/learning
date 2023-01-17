def isSubsequence(s, t):
    inx = 0
    start = 0
    while start != len(t) and inx != len(s):
        if s[inx] == t[start]:
            inx += 1
        start += 1
    return inx == len(s)


print(isSubsequence("", "abc"))
