class Solution(object):
    def searchMatrix(self, matrix, target):
            """
            :type matrix: List[List[int]]
            :type target: int
            :rtype: bool
            """
            for i in matrix:

                if i[0] == target or i[-1] == target:
                    return True

                if i[0] <= target and i[-1] >= target:

                    l = 0
                    r = len(i) - 1

                    while l <= r:
                        mid = (l + r) // 2

                        if i[mid] > target:
                            r = mid - 1
                            continue

                        if i[mid] < target:
                            l = mid + 1
                            continue

                        if target is i[mid]:
                            print(i[mid])
                            return True

                    return False