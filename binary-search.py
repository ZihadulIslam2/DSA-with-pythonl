"""
 test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 13
    },
    'output': 3
}
 def locate_card(cards,query ):
   lo,hi = 0, len(catds )-1
   while lo<= hi :
     mid= (lo+hi )//2
     mid_number = cards[mid ]
     print("lo ",lo, "hi:" , hi, "mid ", mid, "mid_number ", mid_number )
     if mid_number == query :
       return mid
    elif mid_number < query :
      hi = mid-1
    elif mid_number > query :
      lo = mid + 1
  return -1
  """

# Example input and edge cases
test = {
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 0
  },
  'output': 7
}

def locate_card(cards, query):
  lo, hi = 0,len(cards ) -1
  while lo <= hi: 
    mid = (lo+hi ) // 2
    mid_number= cards[ mid]
    print("lo: ",lo, "hi: ", hi, "mid: ", mid, "mid_number ", mid_number)
    if mid_number == query :
      return mid
    elif mid_number < query: 
      hi =mid - 1 
    elif mid_number> query: 
      lo = mid + 1 
  return -1 


# Example call to the function with the input data from the test
result = locate_card(test['input']['cards'], test['input']['query'])
print(result) 