#class Solution:
#     function isPalindrome(s):
#         s = concatenate lowercase alphanumeric characters from s
#         return s is equal to its reverse

# s = create an instance of Solution
# input_string = "A man, a plan, a canal: Panama"
# if isPalindrome of input_string is true:
#     print input_string is a palindrome
# else:
#     print input_string is not a palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum()) # O(n) 
        return s == s[::-1] # the s[::-1] slicing takes O(n)

s = Solution() # O(1)
input_string = "A man, a plan, a canal: Panama" # O(1), 
if s.isPalindrome(input_string): # 0(n), -if statement: O(1))
    print(f"'{input_string}' is a palindrome.") # O(1)
else:
    print(f"'{input_string}' is not a palindrome.") # O(1)
    # Entire Solution: O(n) 

    '''
    The isalnum() method in the code is a built-in Python method that checks
    if a character is alphanumeric. It returns True if the character is alphanumeric 
    (i.e. a letter or a digit) and False otherwise.

    In the code, it's used to filter the characters in the s string, keeping only the
    alphanumeric characters and discarding all other characters (e.g. punctuation marks,
    spaces, etc.). The filtered characters are then joined into a single string using the
    join method.
    '''
  
