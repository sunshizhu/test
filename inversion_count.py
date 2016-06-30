def inversion_count(alist):
#	print ('Splitting', alist)
	counter =0
	if len(alist) >1:
		mid = len(alist)/2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]
		count1 = inversion_count(lefthalf)

		count2 = inversion_count(righthalf)

		i = 0
		j = 0
		k = 0
		counter = count1 + count2
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] <= righthalf[j]:
				alist[k] =lefthalf[i]
				k = k+1
				i = i+1
			else:
				alist[k] = righthalf[j]
				k = k+1
				j = j+1
				counter = counter + (len(lefthalf)-i)
		
		while i < len(lefthalf):
			alist[k] =lefthalf[i]
			k = k+1
			i = i+1
		while j < len(righthalf):
			alist[k] = righthalf[j]
			k = k+1
			j = j+1
	return counter

f=open('./IntegerArray.txt')
line = (f.read().splitlines())

line = map(int, line)



alist = [1,3,5,2,4,6]

alist = line
count = inversion_count(alist)
#print alist
print 'Inversion count is', count
#result was 2407905288



