class Solution(object):
    def isValidSudoku(self, input):

        if self.validateSudokuRules(input) is False:
            return False
        if self.validateSudokuColumn(input) is False:
            return False
        if self.validateSudokuThreeByThree(input) is False:
            return False
        return True




    def validateSudokuColumn(self, arr):
        column = []

        n = 0

        while n < 9:

            box = []
            # n = 0

            for i in range(9):
                box.append(arr[i][n])

                if i == 8:
                    column.append(box)

            n+= 1

        return self.validateSudokuRules(column)

    def validateSudokuRules(self, arr):

        for i in arr:
            obj = {

            }
            for j in i:
                if j == '.':
                    continue
                num = int(j)
                if num < 1 or num > 9:
                    return False
                if num in obj:
                    return False
                obj[num] = 1
        return True

    def validateSudokuThreeByThree(self, arrs):
        threebythree = [arrs[0], arrs[1], arrs[2]]

        arr = [[], [], [], [], [], [], [], [], []]

        for i in range(3):

            # boxxx = [[], [], []]

            for j in range(3):
                if j == 0:
                    a = threebythree[i][0: 3]
                    arr[j] = [*arr[j], *a]

                if j == 1:
                    b = threebythree[i][3: 6]
                    arr[j] = [*arr[j], *b]
                    # arr[j].append(*b)

                if j == 2:
                    c = threebythree[i][6: 9]
                    arr[j] = [*arr[j], *c]
                    # arr[j].append(*c)
        # print(arr)

        threebythree2 = [arrs[3], arrs[4], arrs[5]]

        for i in range(3):

            # boxxx = [[], [], []]

            for j in range(3, 6):
                if j == 3:
                    a = threebythree2[i][0: 3]
                    arr[j] = [*arr[j], *a]

                if j == 4:
                    b = threebythree2[i][3: 6]
                    arr[j] = [*arr[j], *b]
                    # arr[j].append(*b)

                if j == 5:
                    c = threebythree2[i][6: 9]
                    arr[j] = [*arr[j], *c]
                    # arr[j].append(*c)
        # print(arr)
        threebythree3 = [arrs[6], arrs[7], arrs[8]]

        for i in range(3):

            # boxxx = [[], [], []]

            for j in range(6, 9):
                if j == 6:
                    a = threebythree3[i][0: 3]
                    arr[j] = [*arr[j], *a]

                if j == 7:
                    b = threebythree3[i][3: 6]
                    arr[j] = [*arr[j], *b]
                    # arr[j].append(*b)

                if j == 8:
                    c = threebythree3[i][6: 9]
                    arr[j] = [*arr[j], *c]
                    # arr[j].append(*c)

        return self.validateSudokuRules(arr)

