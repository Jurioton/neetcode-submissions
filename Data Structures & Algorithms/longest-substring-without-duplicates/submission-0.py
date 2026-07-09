class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        max_lenght = 0
        left = 0 

        for right in range(len(s)):

            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right])

            max_lenght = max(max_lenght,len(unique))
        return max_lenght