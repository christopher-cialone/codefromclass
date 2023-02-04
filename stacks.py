# when would we use a stack
# whats the point of it?
# stacks inevitably keep track of things in order and manipulate that order


class Solution:
    def removeDuplicates(self, s: str) -> str:
        # make a stack
        # for each character of the string
            # if the stack is empty:
                # add the character to the stack
            # otherwise:
                # look at the top character in the stack
             # if the top character in the stack != the one we are looking at: we found a match
             # add the character we are looking at to the top of the stack
                # otherwise
                # we found a match - remove the top item from the stack
                # return the joined string
        stack = []
        for ch in s:
            print(stack)
            if len(stack) == 0:
                stack.append(ch)
                else:
                    top = stack[-1]
                    if top != ch:
                        stack.append(ch)
                        else:
                            stack.pop()
            return ''.join(stack)
