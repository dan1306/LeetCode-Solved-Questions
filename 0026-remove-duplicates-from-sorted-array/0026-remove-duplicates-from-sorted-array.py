class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        arr = []
        
        obj = {}
        
        for i in range(0, len(nums)):
            if nums[i] in obj:
                arr.append(i)
                
            else:
                obj[nums[i]] = nums[i]
                
        print obj,arr
        
        for j in arr:
            nums[j] = " "
            # nums.a
        
        while " " in nums:
            nums.remove(" ")
        # return nums