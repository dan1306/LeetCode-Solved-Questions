class Solution(object):
    def groupAnagrams(self, arr):

        res = { }
        for i in arr:
            anagram = ''.join(sorted(i))

            if anagram in res:
                res[anagram].append(i)
            else:
                res[anagram] = [i]

        ans = []
        for a in res:
            ans.append(res[a])

        return ans