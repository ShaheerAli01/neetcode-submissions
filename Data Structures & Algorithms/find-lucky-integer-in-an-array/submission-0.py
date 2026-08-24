class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}

        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        largest = -1
        for i in count:
            if count[i] == i:
                largest = max(largest, i)

        return largest



        