def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """

    if a>b and c>b:
         x = b
    if b>a and c>a:
        x = a
    if a>c and b>c:
        
        x = c
    return x
print(main(14,16,24))

    