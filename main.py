class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        not_equal = 0
        not_equal_positions = []
        i = 0

        while i < len(nums):
            if nums[i] == val:
                not_equal += 1
                not_equal_positions.append(i)
            else:
                if len(not_equal_positions) > 0:
                    nums[not_equal_positions[0]] = nums[i]
                    not_equal_positions.remove(not_equal_positions[0])
                    not_equal_positions.append(i)

            i += 1

        for x in range(not_equal):
            x += 1
            nums[x*(-1)] = "_"

        return len(nums) - not_equal


if __name__ == '__main__':
    s = Solution()
    test = [0,1,2,2,3,0,4,2]
    val = 2
    print(s.removeElement(test, val))
