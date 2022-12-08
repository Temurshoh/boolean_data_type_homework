def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    import math
     
    return math.sqrt(a)**2==a
    
print(main(18))
print(main(16))
