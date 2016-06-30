

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
	par = [alist[start],alist[end],alist[(start+end)//2]]
	med = median(par)
	if par[0] == med:
		pos = start
	if par[1] == med:
		pos = end
	if par[2] == med:
		pos = (start+end)//2

	alist[pos],alist[start] = alist[start],alist[pos]
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

def median(data):
    new_list = sorted(data)
    if len(new_list)%2 > 0:
        return new_list[len(new_list)/2]
    elif len(new_list)%2 == 0:
        return (new_list[(len(new_list)/2)] + new_list[(len(new_list)/2)-1]) /2.0


file = open('ex2file.txt','r')
blist = []
for item in file:
	blist.append(int(item))
counter = quicksort(blist)
print counter

#print blist
#prob1 162085
#prob2 160361
#prob3 138382

#alist = [11,9,8,4,3,6,7]
#print alist

#counter = quicksort(alist)
#print alist
#print counter






