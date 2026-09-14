class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = s.split()
        s = "".join(s_list)

        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        s_rev = s[::-1]

        return s.lower() == s_rev.lower()