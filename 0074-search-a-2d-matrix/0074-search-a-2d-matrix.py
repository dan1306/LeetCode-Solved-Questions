class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        n = 0

        for i in matrix:
            
            if i[0] <= target and i[-1] >= target:
                if i[0] == target or i[-1] == target:
                    return True
                arr = [*i]
                l = 0
                r = len(arr) - 1

                # arr.sort()

                print(arr)

                while l <= r:

                    print(l, r)

                    mid = (l + r) // 2

                    if arr[mid] > target:
                        r = mid - 1
                        continue

                    if arr[mid] < target:
                        l = mid + 1
                        continue

                    if target is arr[mid]:
                        print(arr[mid])
                        return True

                return False



                break
        # if len(arr) == 0:
        return False
