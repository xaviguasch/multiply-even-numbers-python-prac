'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(collection):
    evens = 1
    for item in collection:
        if item % 2 == 0:
            evens *= item

    return evens

print(multiply_even_numbers([2,3,4,5,6]))
