"""
# example input edge cases  
test = {
  'input': {
    'cards': [ 13,11,10,7,4,3,1,0]
    'query': 7
  },
  'output': 3
}

def locate_card ():
  position :0 
  
  while True :
    if cards[position ]== query: 
      return position
  position += 1 
  if position == len(cards):
    return -1
  """
  
  # Example input and edge cases
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

def locate_card(cards, query):
    position = 0
    while True:
        if position == len(cards):
            return -1  # If position reaches the end of cards and query isn't found
        if cards[position] == query:
            return position  # Return the position if query is found
        position += 1  # Move to the next position

# Example call to the function with the input data from the test
result = locate_card(test['input']['cards'], test['input']['query'])
print(result)  # Should print 3