def reverse(list1):
	length = len(list1)
	if length <=1:
		return list1
	else:
		last = list1[-1]
		remain = reverse(list1[:-1])

		return [last] + remain


print reverse([1,2,3,4])
