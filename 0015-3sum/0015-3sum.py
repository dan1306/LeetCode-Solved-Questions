class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        soluObj = {}

        nums.sort()
        arr = []

        while len(nums) >= 3:

            initial = 0
            l = initial + 1
            r = len(nums) - 1
            while l != r:
                ans = nums[initial] + nums[l] + nums[r]
                ansArr = [nums[initial], nums[l], nums[r]]
                ansArr.sort()


                if ans == 0:
                    key = f"{ansArr[0]}{ansArr[1]}{ansArr[2]}"

                    if key not in soluObj:
                        soluObj[key] = ansArr
                        arr.append(ansArr)
                    r-= 1
                if ans > 0:
                    r -= 1
                if ans < 0:
                    l += 1
            nums.pop(0)
        # print(soluObj)

#         arr = []

#         for i in soluObj:
           

        return arr