def reverseWords(s):
    slist = s.split()
    head = 0
    tail = len(slist) -1
    while head < tail:
        slist[head], slist[tail] = slist[tail], slist[head]
        head += 1
        tail -= 1
    return ' '.join(slist)

