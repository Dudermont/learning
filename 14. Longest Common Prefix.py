def longestCommonPrefix(strs):
    pref = ""
    for i in range(len(strs[0])):
        for j in strs:
            if i == len(j) or j[i] != strs[0][i]:
                return pref
        pref += strs[0][i]
    return pref


print(longestCommonPrefix(["flower", "flow", "flight"]))
