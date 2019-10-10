def isPalindrome(s) -> bool:
    alphaS = ""
    for x in s:
        if x.isalnum():
            alphaS += x.lower()
    return alphaS == alphaS[::-1]


if __name__ == '__main__':
    print(isPalindrome("1234321"))