import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = s.translate(dict.fromkeys(map(ord, string.punctuation)))
        the_new_str = new_str.replace(' ', '')
        the_string = the_new_str.lower()
        if the_string == the_string[::-1]:
            return True
        else:
            return False