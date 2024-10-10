def lcs(str1, str2, m, n, memo):
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0 or n == 0:
        return 0
    if str1[m - 1] == str2[n - 1]:
        memo[(m, n)] = 1 + lcs(str1, str2, m - 1, n - 1, memo)
        return memo[(m, n)]
    else:
        memo[(m, n)] = max(lcs(str1, str2, m - 1, n, memo), lcs(str1, str2, m, n - 1, memo))
        return memo[(m, n)]


def longestCommonSubsequence(str1, str2):
    memo = {}
    return lcs(str1, str2, len(str1), len(str2), memo)

str1 = "ABCBDAB"
str2 = "BDCAB"
print(f"The length of the Longest Common Subsequence is: {longestCommonSubsequence(str1, str2)}")
