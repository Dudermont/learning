def removeOuterParentheses(s):
    stack = []
    s2 = ""
    for i in s:
        if len(stack) == 0 and i == '(':
            stack.append(i)
            continue
        elif len(stack) == 0 and i == ')':
            continue
        if len(stack) >= 1 and i == ')':
            stack.pop(-1)
            if len(stack) == 0:
                continue
            s2 += i
        else:
            stack.append(i)
            s2 += i
    return s2
