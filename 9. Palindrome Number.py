def isPalindrome(x):
    y = str(x)
    return y == y[::-1]


print(isPalindrome(10))
