def quickSort(alist):
	return quickSortHelper(alist,0,len(alist)-1)


def quickSortHelper(alist,first,last):
	if first<last:
		splitpoint = partition(alist,first,last)
		quickSortHelper(alist,first,splitpoint-1)

		quickSortHelper(alist,splitpoint+1,last)



def partition(alist,first, last):
	pivot = alist[first]

	start = first+1
	end = last
	done = False
	while not done:
		if alist[start]<=pivot and not done:
			start = start +1
		if alist[end]>=pivot and not done:
			end = end-1
		if end < start:
			done = True
		else:
			alist[start],alist[end] = alist[end],alist[start]

	alist[first],alist[end] = alist[end],alist[first]
	return end


alist = [11,9,8,4,3,6,7]
#result = partition(alist,0,len(alist)-1)
#print alist
#print result

quickSort(alist)
print alist




