class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts={}
        for i in nums:
            if i not in dicts:
                dicts[i] = 1
            else:
                dicts[i] += 1 
        

        sorted_dict = sorted(dicts.items(), key=lambda x: x[1],reverse=True)
        l=[]
        for i in range(k):
            l.append(sorted_dict[i][0])
        return l