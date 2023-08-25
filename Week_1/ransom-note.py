# https://leetcode.com/problems/ransom-note/description/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if ransomNote.count(i) <= magazine.count(i):
                pass
            else:
                return False
        return True
