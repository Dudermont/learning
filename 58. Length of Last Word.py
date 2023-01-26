def lengthOfLastWord(s):
    s = s.split()
    return len(s[-1])


print(lengthOfLastWord("   fly me   to   the moon  "))
