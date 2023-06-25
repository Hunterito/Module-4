def make_dict(lst):
    it = reversed(lst)
    d = next(it)
    for n in it:
        d = {n: d}
    return d


print(make_dict([100, 55, 77, 55, 89]))