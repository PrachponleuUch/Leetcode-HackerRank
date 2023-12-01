
def leftRightDifference( nums):
    left = [0]
    right = [0]
    for i in range(len(nums) - 1):
        left = [nums[i] + left[0]] + left
    for i in range(len(nums) - 1):
        right = [nums[-i-1] + right[-i-1]] + right
    left.reverse()
    return [abs(left[i] - right[i]) for i in range(len(nums))]
    """
    :type nums: List[int]
    :rtype: List[int]
    """

print(leftRightDifference([10,4,8,3]))
