from os import *

# working with sets 

class Solution:
    def containsDuplicate(nums: List[int]) -> bool:
         seen = set() # 0(1)
         for num in nums: # 0(n)
            if num in seen: # boolean 0(1)
             return True #0(1)
            else:  # 0()
                seen.add(num) #0(1)
         return False #0(1)
# 0(n)
        
## set: similar to a list, but it cannot contains dupes
# [], set()
# lookups have complexity of 0(1)


# make a set of numbers to represent what we have seen before
#loop thru our nums list
# for loop:
    #if that number is in our set
    #return true
    #else, we need to add it to our set
    #return true


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Create a dictionary to store the count of each element in the list
        count_dict = {}
        # Iterate over the list
        for num in nums:
            # If the element is not in the dictionary, add it and set its count to 1
            if num not in count_dict:
                count_dict[num] = 1
            # If the element is already in the dictionary, increment its count
            else:
                count_dict[num] += 1
                
            # If the count of the current element is greater than n / 2, return it
            if count_dict[num] > len(nums) // 2:
                return num


