class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        setOfN = set(nums);

        l = 0;
        
        for i in setOfN:

            if i - 1 not in setOfN:
                length = 1;
                placeHolder = i + 1;
                while placeHolder in setOfN:
                    length += 1;
                    placeHolder += 1;
                if length > l:
                    l = length;

        return l;