class Solution:
    alphabet = "qwertyuiopasdfghjklzxcvbnm0123456789"
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].lower() not in self.alphabet:
                left += 1
                continue
            if s[right].lower() not in self.alphabet:
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                print(s[left], s[right])
                return False
            
            left += 1
            right -= 1

        return True