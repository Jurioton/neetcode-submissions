from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = Counter(word)

            key = tuple(sorted(count.items()))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())



        
            


        