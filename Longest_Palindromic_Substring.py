def longestPalindrome(s):
    current_longest = [0,1]

    for i in range(1,len(s)):
        Odd = isLongestPalindrom(s,i-1,i+1)
        Even = isLongestPalindrom(s,i-1,i)

        longest = max(Odd, Even, key=lambda x: x[1] - x[0])
        current_longest = max(current_longest,longest,key=lambda x:x[1]-x[0])
    return s[current_longest[0]:current_longest[1]]

def isLongestPalindrom(sub,left,right):
    while left >=0 and right < len(sub):
        if sub[left] != sub[right]:
            break
        else:
            left-=1
            right+=1
    return [left+1,right]


if __name__ == '__main__':
    #print(isLongestPalindrom("3aba3",1,3))
    print(longestPalindrome("cbbabbd"))