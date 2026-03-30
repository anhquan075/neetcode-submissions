class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_opens = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char not in close_to_opens:
                stack.append(char)
            else:
                if stack and stack[-1] == close_to_opens[char]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
