def BinaryTree(r):
	return [r,[],[]]

def insertLeft(root,newBranch):
	t = root.pop(1)

	if len(t)>1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[],[]])
	return root

def insertRight(root,newBranch):
	t=root.pop(2)
	if len(t)>1:
		root.insert(2,[newBranch,[],t])
	else:
		root.insert(2,[newBranch,[],[]])

	return root


def getRootVal(root):
	return root[0]

def setRootVal(root,newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

def testEqual(val,tarval):
	if val == tarval:
		print True
	else:
		print "dismatch occurred"

r = BinaryTree('a')
insertLeft(r,'b')
insertRight(getLeftChild(r),'d')
insertRight(r,'c')
s = getRightChild(r)
insertLeft(s,'e')
insertRight(s,'f')
  


ttree = r
testEqual(getRootVal(getRightChild(ttree)),'c')
testEqual(getRootVal(getRightChild(getLeftChild(ttree))),'d')
testEqual(getRootVal(getRightChild(getRightChild(ttree))),'f')

