def factorial(x):
    
    j = x - 1

    while j > 0:

        x *= j
        j -= 1

    return x
