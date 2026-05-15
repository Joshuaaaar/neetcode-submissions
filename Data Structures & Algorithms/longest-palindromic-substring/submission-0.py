class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        start = 0
        maxLen = 1

        # length 1
        for i in range(n):
            dp[i][i] = True

        # length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                maxLen = 2

        # length >= 3
        for length in range(3, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                if s[i] == s[j] and dp[i + 1][j - 1]:

                    dp[i][j] = True

                    if length > maxLen:
                        start = i
                        maxLen = length

        return s[start:start + maxLen]