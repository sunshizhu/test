import random

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

#    def combine(self, f,t): #combine f and t

    	
#    for item in self.vertList[t].connectedTo()

#    	del self.vertList[t]
#    	return

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())




file = open('array.txt','r')
doc = []
g = Graph()
for line in file:
	line = line.split()
	g.addVertex(line[0])
	for pt in line[1:]:
		g.addEdge(line[0],pt)

#print g.vertList['2'].connectedTo

for v in g:
	for w in v.getConnections():
		print w
		print "(%s %s)"%(v.getId(),w.getId())



del g.vertList['2']
#print g.vertList