def positive_divide(numerator, denominator):
    try:
        answer = numerator/denominator
        if answer < 0:
            raise ValueError("Invalid type")
        return answer
    except ZeroDivisionError:
        return 0        
    except TypeError as te:
        if "unsupported operand" in str(te):
            raise te
        


#Value Errors
print(positive_divide(1, -2))
print(positive_divide(-1, 2))

'''
#Type Error tests
#print(positive_divide(1, 's'))
#print(positive_divide([], 2))
'''

#print(positive_divide(2, 0))

#test 1
'''
These work
print(positive_divide(1, 2))
print(positive_divide(1, 0))
print(positive_divide(-1, -2))
print(positive_divide(1.5, 2))
'''

'''

Write division function that:

1. When the denominator is zero, catch the corresponding exception and return zero.

2. When the numerator or denominator have an invalid type reraise the corresponding exception.

3. If the result of the division is negative raise a ValueError.
'''

#Tests
'''
def test_positive_divide_good_values():
    assert positive_divide(1, 2) == 0.5
    assert positive_divide(1, 0) == 0
    assert positive_divide(-1, -2) == 0.5
    assert positive_divide(1.5, 2) == 0.75

def test_positive_divide_exceptions():
    try:
        positive_divide(2, 0)
    except ZeroDivisionError:
        pytest.fail("Unexpected ZeroDivisionError!")
    with pytest.raises(TypeError):
        positive_divide(1, 's')
        positive_divide([], 2)
    with pytest.raises(ValueError):
        positive_divide(1, -2)
        positive_divide(-1, 2)
'''