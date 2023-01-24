def isValid(s):
    stak = []
    close_to_open = {"]": "[", ")": "(", "}": "{"}
    for i in s:
        if i in close_to_open:
            if stak and stak[-1] == close_to_open[i]:
                stak.pop()
            else:
                return False
        else:
            stak.append(i)
    return True if not stak else False


print(isValid("()]{}"))
