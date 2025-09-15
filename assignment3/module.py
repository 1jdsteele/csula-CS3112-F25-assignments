#problem 1: merge sort






# problem 3
def take_exponenet(base: int, exponent: int) -> int:
    if exponent == 0: return 1
    if exponent == 1: return base
    # to make next parts more efficient, turn the half into avar and then multiply to itself
    if exponent % 2 == 1:
        return base * take_exponenet(base, int((exponent - 1) / 2)) * take_exponenet(base, int((exponent - 1) / 2))
    return take_exponenet(base, exponent // 2) * take_exponenet(base, exponent // 2)