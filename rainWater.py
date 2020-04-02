import json

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        lakes = []
        left_height = height[0]
        left_index = 0
        right_height = 0
        right_index = -1
        down = False
        for i in range(1, len(height)):
            if not down:
                if left_height >= height[i]:
                    down = True
                else:
                    left_height = height[i]
                    left_index = i
            else:
                if height[i] >= left_height:
                    right_height = height[i]
                    right_index = i
                    down = False
                    lakes.append((left_index, right_index, min(left_height, right_height)))
                    left_height = right_height
                    left_index = right_index
                    right_height = 0
                    right_index = len(height) - 1
                else:
                    if height[i] >= right_height:
                        right_height = height[i]
                        right_index = i
        print(lakes)
        if down:
            lakes.append((left_index, right_index, min(left_height, right_height)))
            print(lakes)
            left_height = right_height
            left_index = right_index
            end = left_index
            end_height = left_height
            right_height = height[-1]
            right_index = len(height) - 1
            down = False
            for i in range(len(height) - 2, end, -1):
                if not down:
                    if right_height >= height[i]:
                        down = True
                    else:
                        right_height = height[i]
                        right_index = i
                else:
                    if height[i] >= right_height:
                        left_height = height[i]
                        left_index = i
                        down = False
                        lakes.append((left_index, right_index, min(left_height, right_height)))
                        right_height = left_height
                        right_index = left_index
                        left_height = end_height
                        left_index = end
                    else:
                        if height[i] >= left_height:
                            left_height = height[i]
                            left_index = i
            if down:
                lakes.append((left_index, right_index, min(left_height, right_height)))
        total_water = 0
        print(lakes)
        for l in lakes:
            for i in range(l[0] + 1, l[1]):
                total_water += max(0, l[2] - height[i])

        return total_water


def stringToIntegerList(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            height = stringToIntegerList(line)

            ret = Solution().trap(height)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()