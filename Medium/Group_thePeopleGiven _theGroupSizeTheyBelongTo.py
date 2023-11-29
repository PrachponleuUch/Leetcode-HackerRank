def groupThePeople(groupSizes):
  group_map = {}
  result = []
  
  # groupsize is key, person is value that is add to the key in form of a list
  for person, groupsize in enumerate(groupSizes):
    group_map[groupsize] = group_map.get(groupsize, []) + [person] 
  
  # split people with the same group size into groups based on their group size
  for groupsize, people in group_map.items():
    for i in range(0, len(people), groupsize):
      result.append(people[i:i+groupsize]) 
  return result
  """
  :type groupSizes: List[int]
  :rtype: List[List[int]]
  """