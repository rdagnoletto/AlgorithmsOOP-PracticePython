class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        str_len = len(s)
        even = str_len % 2 == 0

        char_count = dict()
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        found_odd = False
        middle = None
        for c in char_count.keys():
            n = char_count[c]
            char_count[c] = n // 2
            if n % 2 != 0:
                if even or found_odd:
                    return []
                else:
                    found_odd = True
                    middle = c

        if not even and not found_odd:
            return []

        strings = self.palRecursive(char_count)

        end_strings = []

        for s in strings:
            string = s
            rev = s[::-1]
            if middle:
                string += middle
            string += rev
            end_strings.append(string)

        return end_strings

    def palRecursive(self, char_count, strings=None):
        if strings is None:
            strings = [""]

        end_strings = []
        non_zero = False
        for c in char_count.keys():
            if char_count[c] > 0:
                temp = char_count.copy()
                temp[c] = char_count[c] - 1
                non_zero = True
                next_strings = []
                for s in strings:
                    next_strings.append(s + c)
                end_strings += self.palRecursive(temp, next_strings)
        if not non_zero:
            end_strings = strings
        return end_strings


