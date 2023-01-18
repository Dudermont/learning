def romanToInt(s):
    s = list(s)
    s.reverse()
    s.append("T")
    total = 0
    count = 0
    for i in range(len(s)):
        if s[i + count] == "I":
            total += 1
        elif s[i + count] == "V":
            if s[i + count + 1] == "I":
                total += 4
                count += 1
            else:
                total += 5
        elif s[i + count] == "X":
            if s[i + count + 1] == "I":
                total += 9
                count += 1
            else:
                total += 10
        elif s[i + count] == "L":
            if s[i + count + 1] == "X":
                total += 40
                count += 1
            else:
                total += 50
        elif s[i + count] == "C":
            if s[i + count + 1] == "X":
                total += 90
                count += 1
            else:
                total += 100
        elif s[i + count] == "D":
            if s[i + count + 1] == "C":
                total += 400
                count += 1
            else:
                total += 500
        elif s[i + count] == "M":
            if s[i + count + 1] == "C":
                total += 900
                count += 1
            else:
                total += 1000
        else:
            return total


print(romanToInt("MCMXCIV"))
