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
    
    if (a>b and b>c) or (c>b and b>a) or (b==a and c==b):
        x=b
    if (b>a and a>c) or (c>a and a>b) or (a==b and c==a):
        x = a
    if (a>c and c>b) or (b>c and c>a) or (c==b and c==a ):
        x = c

    return x
     
print(main(21,17,13))

     