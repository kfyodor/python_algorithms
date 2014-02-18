def gcd(a, b):
    if b > a:
        _a, _b = a, b
    else:
        _a, _b = b, a

    if _a == 0:
        return _b
    else:
        return gcd(_a, _b % _a)