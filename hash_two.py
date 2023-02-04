class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dict = {}
        for n in s:
            if i in count_dict:
                count_dict += 1
            else:
                count_dict = 1
       
        
        for ibex, ch in enumerate(s):
            if count_dict[ch] == 1:
                return ibex

