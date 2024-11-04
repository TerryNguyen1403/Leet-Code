def isAnagram(s, t):
    if len(s) != len(t):
        return False

    countS = {}
    countT = {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)

    return countS
