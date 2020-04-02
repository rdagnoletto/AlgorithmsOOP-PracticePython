class Solution(object):
    def decodeString(self, s):
        mult = ["1"]
        strings = [""]
        indig = False
        for c in s:
            if c.isdigit():
                if indig:
                    mult[-1] += c
                else:
                    mult.append(c)
                    indig = True
            elif c == "[":
                indig = False
                strings.append("")
            elif c == "]":
                m = int(mult.pop())
                st = strings.pop()
                strings[-1] += m * st
            else:
                strings[-1] += c
        return strings[0]
