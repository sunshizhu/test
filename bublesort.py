def bubblesort(alist):
	for item in range(len(alist)-1, 0,-1):
		for i in range(item):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]


alist = [54,26,93,17,77,31,44,55,20]
bubblesort(alist)
print(alist)
