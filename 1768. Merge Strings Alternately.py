def mergeAlternately(word1, word2):
    index = 0
    word3 = ""
    while index < len(word1) or index < len(word2):
        if index < len(word1):
            word3 += word1[0 + index]
        if index < len(word2):
            word3 += word2[0 + index]
        index += 1
    return word3
