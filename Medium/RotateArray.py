def rotate(nums, k):
  length = len(nums)
  nums[:] = nums[-k%length:] + nums[:-k%length]
  return nums