class Solution:
    def __init__(self):
        self.datas = [['microsoft', -20, 2], ['verde', 4, 4], ['soundly', -20, 2]]

    def rev_profit(self):
        """return the latest biz with the largest profit"""
        largest = float('-inf')
        index = 0
        for count, element in enumerate(self.datas):
            profit = element[1] - element[2]
            if (profit >= largest):
                largest = profit
                index = count
        return self.datas[index]

# Can we do this with a comprehension?

print(Solution().rev_profit()[0])
