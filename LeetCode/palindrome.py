def longestPalindrome( s: str):
    longest = '' if not s else s[0]
    max_len = 1
    size = len(s)
    dp = [[False] * size for _ in range(size)]
    for start in range(size - 1, -1, -1):
        dp[start][start] = True
        for end in range(start + 1, size):
            if s[start] == s[end]:
                if end - start == 1 or dp[start + 1][end - 1]:
                    dp[start][end] = True
                    if max_len < end - start + 1:
                        max_len = end - start + 1
                        longest = s[start: end + 1]
    return longest

s="babad"
pn= longestPalindrome(s)
print(pn)