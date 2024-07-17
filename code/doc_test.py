def soma(x, y):
    """soma x e t

    >>> soma(32, 13)
    45
    """
    return x+y

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)