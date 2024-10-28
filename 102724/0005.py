class Solution:
  # so brute force would be o(n^3) becasuse we know that to generate every substring whould require looping through parameters (double for loops) then each one is checking if it is a paliendrome.
  # to get it down, we can use one parameter to loop through centerpoints and then check if there is a paliendrome steming from a center point, which would make it O(n^2)
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right): # helper function with a right and left pointer that moves out as long as they are in the range of the string and are still equal to eachother
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = "" # this will track the longest strings as we go
        
        for i in range(len(s)): # i in this case represents the middle index which we will loop through as we go throughout the string then compare the resulting paliendrome length to what we get.
            # since there are two cases where the paliendrome is starting from a letter in the middle and when the paliendrome is from 2 letters on either side we had to run the expand function twice, once with the same right and left pointers and once with the right pointer incremented
            odd_palindrome = expand(s, i, i)
            even_palindrome = expand(s, i, i + 1)

            # now that we have the two potential paliendrome canidates, check if they are bigger than the cur longest
          
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest
