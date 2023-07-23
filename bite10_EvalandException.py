def divide_numbers(numerator, denominator):
    try:
        num = int(numerator)
        den = int(denominator)
        answer = num/den
        
    except ValueError:
        raise ValueError("Invalid numerator or denominator.")
    except ZeroDivisionError:
        return 0
    return answer

print(divide_numbers(10, 0))


'''complete the divide_numbers function that takes a numerator and a denominator (the number above and below the line respectively when doing a division).

First you try to convert them to ints, if that raises a ValueError you will re-raise it (using raise).

To keep things simple we can expect this function to be called with int/float/str types only (read the tests why ...)

Getting passed that exception (no early bail out, we're still in business) you try to divide numerator by denominator returning its result.

If denominator is 0 though, Python throws another exception. Figure out which one that is and catch it. In that case return 0.'''