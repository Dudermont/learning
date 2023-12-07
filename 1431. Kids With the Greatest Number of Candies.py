def kidsWithCandies(candies, extraCandies):
    m = max(candies)
    result = []
    for i in candies:
        if i + extraCandies >= m:
            result.append(True)
        else:
            result.append(False)
    return result
