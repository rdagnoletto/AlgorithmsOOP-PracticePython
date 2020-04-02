class Solution(object):
    def wordBreak(self, s, wordDict, first=True):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if first:
            new_dict = []
            for w in wordDict:
                if w in s:
                    new_dict.append(w)
            wordDict = sorted(new_dict, key=len)

        if not s:
            return True
        for w in wordDict:
            if s.startswith(w):
                if self.wordBreak(s[len(w):], wordDict, False):
                    return True

        return False