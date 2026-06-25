class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
    
        if len(matrix) == 0:
            return -1
   
        first = 0
        last = len(matrix) - 1
        middle = (first + last) // 2

        while first <= last:

            if matrix[middle][0] > target :
                last = middle -1
            elif matrix[middle][len(matrix[middle]) - 1] < target:
                first = middle + 1
            else:
                if self.search(matrix[middle], target) != -1:
                    print("t")
                    return True
                else:
                    print("f")
                    return False
                
            middle = (first + last) // 2



        return False
        

        

    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
   
        first = 0
        last = len(nums) - 1
        middle = (first + last) // 2

        while first <= last:

            if nums[middle] == target:
                return middle

            elif nums[middle] > target:
                last = middle -1
            elif nums[middle] < target:
                first = middle + 1
            middle = (first + last) // 2



        return -1
