#def func(string: str) -> bool:
#    return True if string == string[-1::-1] else False

func = lambda string: True if string == string[-1::-1] else False


print(func(input()))