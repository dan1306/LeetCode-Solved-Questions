class Solution(object):
    def search(self, nums, target):
        beg = 0
        end = len(nums) - 1

        mid =int(round((beg + end)/2))
        # print(mid)

        while beg < end:

            if nums[mid] == target:
                print(mid)
                return mid

            elif nums[mid] > target:
                print(nums[mid], target)

                end = mid - 1
            else:
                print('beg')

                beg = mid + 1

            mid = int(round((beg + end) / 2))


        if nums[mid] == target:
            print(mid, nums[mid])
            return mid
        else:
            print(-1)
            return -1

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        