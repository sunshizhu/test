class Heap:
	def __init__(self):
		self.size = 0
		self.heaplist = [0]

	def percUp(self,i):
		while i//2 >0:
			if self.heaplist[i//2] > self.heaplist[i]:
				self.heaplist[i//2], self.heaplist[i] = self.heaplist[i],self.heaplist[i//2]
			i = i//2


	def insertkey(self,k):
		self.heaplist.append(k)
		self.size = self.size +1
		self.percUp(self.size)

	def findMin(self):
		return self.heaplist[1]


	def percDown(self,i):
		while i*2<=self.size:
			minc = self.minChild(i)
			if self.heaplist[i] > self.heaplist[minc]:
				self.heaplist[i], self.heaplist[minc] = self.heaplist[minc], self.heaplist[i]
				i = minc
			else: break
		return

	def minChild(self,i):
		if i*2+1 > self.size & i*2 <= self.size:
			return i*2
		else:
			if self.heaplist[i*2] < self.heaplist[i*2+1]:
				return i*2
			else:
				return i*2+1


	def delMin(self):
		self.heaplist[1] = self.heaplist[self.size]
		self.size = self.size -1
		self.heaplist.pop()
		self.percDown(1)

		return

	def buildHeap(self, inputarray):
		#self.size = len(inputarray)
		for item in inputarray:
			print item
			self.insertkey(item)
		return





bh = Heap()
lol = [5,2,7,4,78,3,1]
bh.buildHeap(lol)

bh.insertkey(5)
bh.insertkey(7)
bh.insertkey(6)
bh.insertkey(11)
bh.insertkey(4)
bh.insertkey(1.5)
bh.delMin()
print bh.heaplist
print bh.findMin()
