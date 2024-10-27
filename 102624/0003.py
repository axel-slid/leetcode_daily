class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

# notes:
# well i didn’t initially know that a sliding window would be the answer here
# this is going to be a theme for a log of them there is a left pointer and a right pointer, then we just compare substring lengths, probably the only way to do it faster is do it from the one point out then keep going, not rlly sure tho.
# sets let you do it in o(n)
