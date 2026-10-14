def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a = n // 10000
    b = (n // 1000) % 10
    c = (n // 100) % 10
    d = (n // 10) % 10
    e = n % 10
    i = 0
    if a > b and a > c and a > d and a > e :
        i = 1
        return a
    elif b > a and b > c and b > d and  b > e :
        i = 2
        return b
    elif   d > a and d > b and  d > c and d > e :
        i = 3
        return d
    elif c > a and c > b and c > d and c > e :
        i = 4
        return c
    elif e > a and e > b and e > c and e > d :
        i = 5
        return e
      
print(main(76514))