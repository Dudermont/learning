def uniqueOccurrences(arr):
    count_dict = {}
    for i in arr:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return len(count_dict) == len(list(set(count_dict.values())))
