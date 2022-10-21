def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    
    if (a>b and b>c) or (c>b and b>a):
        return b
    elif (b>a and a>c) or (c>a and a>b):
        return a
    elif (a>c and c>b) or (b>c and c>a):
        return c
    else:
        return a
print(main(5,5,-1))

     