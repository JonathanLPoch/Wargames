def func5(firstNum, secondNum, thirdNum):
	v3 = (thirdNum - secondNum)/2
	v4 = v3 + secondNum
	if(v3 + secondNum <= firstNum):
		result = v3 + secondNum
		if(v4 < firstNum):
			result = v4 + func5(firstNum, v4 + 1, thirdNum)
	else:
		result = v4 + func5(firstNum, secondNum, v4 - 1)
	return result


for firstNum in range(0, 15):
	print "For ", firstNum, ":", func5(firstNum, 0, 14)



