def quicksort(alist):
	counter = 0
	counter = sorting(alist,0, len(alist)-1, counter)

	return counter


def sorting(alist,starting, ending,counter):
	if starting < ending:
		ppoint,counter = partition(alist,starting,ending,counter)
		#print 'partition point is %d'%alist[ppoint]
		
		counter =sorting(alist,starting,ppoint-1,counter)
		counter = sorting(alist,ppoint+1,ending,counter)
	#	print alist
	return counter

def partition(alist,start,end,counter):
	target = alist[end]
	j = start
	i = start

	while j<end:
		counter = counter +1
		#print counter
		if alist[j]< target:
			alist[j],alist[i] = alist[i],alist[j]
			i = i+1
		j = j+1
	alist[end],alist[i] = alist[i],alist[end]
	#alist[end],alist[start] = alist[start],alist[end]

	return i, counter


file = open('ex2file.txt','r')
blist = []
for item in file:
	blist.append(int(item))
counter = quicksort(blist)
print counter

#print blist
#prob1 162085
#prob2 160361


#alist = [11,9,8,4,3,6,7]
#print alist

#quicksort(alist)
#print alist






