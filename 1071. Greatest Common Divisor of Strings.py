def gcdOfStrings(str1, str2):
    m, n = len(str1), len(str2)

    def valid(r):
        if m % r or n % r:
            return False
        o1, o2 = m / r, n / r
        gcd = str1[:r]
        return str1 == o1 * gcd and str2 == o2 * gcd
    for i in range(min(m, n), 0, -1):
        if valid(i):
            return str1[:i]
    return ''
