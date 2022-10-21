def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a==b:
        m= 0
    if a>b:
        m=a
    if b>a:
        m=b
        return m
     
    

    print(main(45,56))