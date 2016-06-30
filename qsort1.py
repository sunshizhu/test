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
	target = alist[start]
	j = start+1
	i = start+1

	while j<=end:
		counter = counter +1
		#print counter
		if alist[j]< target:
			alist[j],alist[i] = alist[i],alist[j]
			i = i+1
		j = j+1
	alist[start],alist[i-1] = alist[i-1],alist[start]

	return i-1, counter


file = open('ex2file.txt','r')
blist = []
for item in file:
	blist.append(int(item))
#print blist
counter = quicksort(blist)
print counter
#print blist
#prob1 162085


#alist = [11,9,8,4,3,6,7]
#result = partition(alist,0,len(alist)-1)
#print alist
#print result
#quicksort(alist)
#print alist






