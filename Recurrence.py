# without memoize, it would take a couple of minutes to finish for (30, 3).
def number(position, increment_multiplier, memoize_dict):
    if position in memoize_dict:
        return memoize_dict.get(position), memoize_dict

    result = 0
    mem_dict = memoize_dict

    if position > 0:
        first, mem_dict = number(position - 1, increment_multiplier, mem_dict)
        second, dummy = number(position - 2, increment_multiplier, mem_dict)
        result = first + increment_multiplier * second

    if position == 0:
        result = 1

    if position < 0:
        result = 0

    mem_dict = dict(mem_dict)
    mem_dict[position] = result

    return result, mem_dict


# Compared to rosalind FIB task, this algo should be provided with (n-1, k) to give accepted results
res, mem = number(30, 3, {})
print res
