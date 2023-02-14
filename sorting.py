class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:



    a_list = [5,4,3,2,1]
    b_list = [5,4,3,2,1]
    a_list.sort()
    print('after using sort()', a_list)

    new_list = sorted(b_list)
    print('after using sorted()', b_list, new_list)

def sortPeople(names, heights):

    height_dict = dict(zip(heights, names))
    results = []
    print(height_dict)

sortPeople(["a", "b", "c"], [1, 3, 2])



    # one thing I want to stress is keeping the name and ehights together 

    # pseudocode:
    # use a dictionary to make sure names and heights stay associated with each other
    # make a dictionary and put our two lists into it
    # place names and heights into dictionary
    # make result list
    # sort our dictionary
    # for loop
        # add names to our result list, in order of the new sorted heights


        '''
        You are given an array of strings names, and an array heights that consists of distinct 
        positive integers. Both arrays are of length n.

        For each index i, names[i] and heights[i] denote the name and height of the ith person.

        Return names sorted in descending order by the people's heights.

 

        Example 1:

        Input: names = ["Mary","John","Emma"], heights = [180,165,170]
        Output: ["Mary","Emma","John"]
        Explanation: Mary is the tallest, followed by Emma and John.
        Example 2:

        Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
        Output: ["Bob","Alice","Bob"]
        Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
        

        Constraints:

        n == names.length == heights.length
        1 <= n <= 103
        1 <= names[i].length <= 20
        1 <= heights[i] <= 105
        names[i] consists of lower and upper case English letters.
        All the values of heights are distinct.
        Accepted
        60.3K
        Submissions
        74.1K

        '''