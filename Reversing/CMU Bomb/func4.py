def func4(a1):
    result = 0
    if(a1 <= 1):
	result = 1
    else:
        v1 = func4(a1-1)
	result = v1 + func4(a1-2)
    return result

print func4(9)
