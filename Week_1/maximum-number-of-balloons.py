# https://leetcode.com/problems/maximum-number-of-balloons/


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = 1
        a = 1
        l = 2
        o = 2
        n = 1
        lst = []
        for i in "balon":
            my_var = eval(i)
            if i in text:
                lst.append(text.count(i) // eval(i))
            else:
                return 0
        return (min(lst))
