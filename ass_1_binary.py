"""
state:
- i need to find the small number.
- find the middle number.
- if the mid num small then before, it is the smallest num.
- if not, I need to decide which side
- check if the mid num smaller then the lust num. than go left.
- if the mid num bigger than the num. go right
- 
"""

def rotation_counter(num):
    low = 0
    hi = len(num) - 1  # hi should be the last index, not length

    while low <= hi:
        mid = (low + hi) // 2  # Correct mid calculation
        mid_number = num[mid]

        # Check if mid_number is the smallest
        if mid > 0 and mid_number < num[mid - 1]:
            return mid
        # Decide which side to go
        elif mid_number < num[hi]:
            hi = mid - 1  # Search left
        else:
            low = mid + 1  # Search right

    return 0  # Default return if no rotation

# Test case
test = {
    'input': {
        'num': [7, 8,9,10, 1, 3, 4, 5, 6]
    },
    'output': {
        'rotaionum': 2
    }
}

result = test['input']['num']
print(rotation_counter(result))  # Should print 2



"""
test = {
    'input': {
        num: [7,8,1,3,4,5,6]
    },

    'output': {
        rotaionum: 2
    }
}

def rotation_counter (num):
    low = 0
    hi = len(num)-1

    while hi>=low:
        mid = low + hi // 2
        mid_number = num[mid]

        if mid > 0 and mid_number < num[mid-1]:
            return mid
        elif mid_number < num[hi-1]:
            hi = mid - 1
        else :
            low = mid + 1
    return 0
            
result = test['input'] ['num']

print(rotation_counter(result))
"""