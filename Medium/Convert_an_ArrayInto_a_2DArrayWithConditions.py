

def findMatrix(nums):
  matDict = {}
  result = []
  for num in nums:
    matDict[num] = matDict.get(num, 0) + 1
  
  for num, amount in matDict.items():
    while len(result) < amount:
      result.append([])
    while amount > 0:
      result[amount-1].append(num)
      amount -= 1
    
  return result

  """
  :type nums: List[int]
  :rtype: List[List[int]]
  """
        
