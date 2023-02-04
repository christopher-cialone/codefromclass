class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
  
        unique_emails = set()                        # O(1)
        for email in emails:                         # O(n)
            local, domain = email.split("@")         # O(m)
            local = local.replace(".", "")           # O(m)
            plus_index = local.find("+")             # O(m)
            if plus_index != -1:                     # O(1)
                local = local[:plus_index]           # O(m)
            unique_emails.add(f"{local}@{domain}")   # O(1)
        return len(unique_emails)                    # O(1)
# The overall time complexity is O(n * m) in worst case, O(n + m) in 
# the average case
'''
The solution utilizes a set to keep track of unique email addresses. It splits each email into
its local and domain parts using split("@"). The dots in the local part are then eliminated 
using replace(".", ""). If there is a "+" symbol, everything after it is removed, including
the "+" symbol itself. The unique email address in the format of {local}@{domain} is then
added to the set. After processing all the emails, the number of unique email addresses
is returned as the length of the set.
 '''

'''
The overall time complexity is O(n * m) in the worst case and O(n + m) in the average case because
for each email, the code performs operations that take O(m) time, such as splitting the email into
two parts, replacing the "." in the local part, and finding the index of the "+" symbol in the
local part. And it performs an O(1) add operation for each unique email to add it to the set. 
So for all emails, the time complexity is O(n * m) in the worst case, if all emails are different
and O(n + m) in the average case, if some emails are the same.
'''