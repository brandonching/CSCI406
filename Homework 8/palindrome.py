# Write a “top-down” DP solution that augments the recursive algorithm above with memoization. Store intermediate results in a dictionary/array and check to see if a value has already been determined before computing it again. If the value has already been computed, then return it instead of making the recursive call(s).

# The function should return the length of the longest palindromic subsequence in the string.

def longest_palindromic_substring(S):
    memo = {}

    def dp(i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if (i, j) not in memo:
            if S[i] == S[j]:
                memo[i, j] = dp(i + 1, j - 1) + 2
            else:
                memo[i, j] = max(dp(i, j - 1), dp(i + 1, j))
        return memo[i, j]
    return dp(0, len(S) - 1)


# Test cases
print(longest_palindromic_substring("bbbab"))  # 4
print(longest_palindromic_substring("cbbd"))  # 2
print(longest_palindromic_substring("a"))  # 1
print(longest_palindromic_substring("racecar"))  # 1
print(longest_palindromic_substring("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget ex felis. Proin non augue ligula. Vivamus nec metus sed metus consequat tincidunt. Nam lacinia neque vitae luctus vulputate. Nulla facilisi. Integer non suscipit libero. Donec sed leo nec mi tincidunt gravida vel ut justo. Sed eu justo sed nibh volutpat facilisis. Nam id augue ut magna rutrum feugiat at sit amet nisi. Quisque sit amet metus quis nunc dictum facilisis. Aenean ut eros ex. Phasellus sed turpis ut nisi bibendum condimentum. Mauris ullamcorper velit at libero interdum, eu vehicula libero fringilla. Nunc ac lorem vel sapien suscipit varius sit amet vel purus. Suspendisse ultricies consequat turpis, sed blandit justo ullamcorper in. Proin tempus metus in mi tempus, at ultricies dolor bibendum. Nulla sit amet massa ullamcorper, convallis ligula nec, suscipit justo. Integer malesuada sapien eget metus ultricies, quis finibus libero dapibus."))
