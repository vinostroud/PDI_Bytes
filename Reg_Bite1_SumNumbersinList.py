
def sum_numbers(numbers):
    list_sum = 0
    if numbers == None:
        return sum(range(0,101))
    
    else: 
        for i in numbers:
            list_sum = list_sum + i
    return list_sum

print(sum_numbers([]))

'''
Write a Python function that calculates the sum of a list of numbers:

The function should accept a list of numbers and return the sum of those numbers.
If no argument is provided (that is, numbers is None), return the sum of the numbers 
1 to 100 (Note that this is not the same as an empty list of numbers being passed in. In that case the sum returned will be 0).

'''
        
