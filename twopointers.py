   # Input: s = ['h', 'e', 'l', 'l', 'o']
   # Output: ['o', 'l', 'l', 'e', 'h']


class Solution:
    def reverseString(self, s: List[str]) -> None:
        n =len(s)
        i = 0
        j = n-1

        while i < n/2:
            print(i, j, n//2)
            i+=1
            j-=1

            #while i < n/2:
            for i in range(n/2):
                print(i, j)
                s[i], s[j] = s[j], s[i]
                print(s)
                i+=1
                j-=1
                #longer solution
                #temp = s[i]
                #s[i] = s[j]
                #s[j] = temp
        """
        Do not return anything, modify s in-place instead.
        """
        # Input: s = ['h', 'e', 'l', 'l', 'o']
        # Output: ['o', 'l', 'l', 'e', 'h']
        '''
        one pointr at the beginnning of the list, one point at the end of the list
        while loop
        loop through n/2
        take pointer i, and switch that element with the one at pointer
        increase point i, decrease point j
        return the answer
        '''


# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1