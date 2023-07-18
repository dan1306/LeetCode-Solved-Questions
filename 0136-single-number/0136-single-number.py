class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hashMap = {}
        
        for i in nums:
            if str(i) in hashMap:
                hashMap[str(i)] += 1
            else:
                 hashMap[str(i)] = 1
                    
        print(hashMap)
        
        for i in hashMap:
            if hashMap[i] == 1:
                return int(i)
#         ans = []
#         pre = None
        
#         for i in nums:
#             if len(ans) == 0 and pre is not i:
#                 pre = i
#                 ans[0] = i
#             else:
#                 ans.pop(0)
                
#         return ans[0]