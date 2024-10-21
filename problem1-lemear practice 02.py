# example input output edge cases

test = {
  'input': {
    'cards': [13,11, 10, 7, 4, 3, 1, 0],
    'query': 0 
  },
  'output': 3
}

"""
state:
1. create variable position 0
2. check number = query
3. if match, return position
4. if doesnt incriment the position.
5. if non of tham match return -1 
"""

# implement the solution

def locate_card ( cards, query ):
  position = 0 
  while True:
    if cards[position] == query :
      return position
      
    position += 1 
  if position == len(cards):
    return -1 
  
  
result = locate_card ( test['input']['cards'] , test['input']['query'])

print(result )