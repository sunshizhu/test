import random
import time

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

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def loadGraph():
	file = open('array.txt','r')
	G = Graph()
	for line in file:
		line = line.split()
		tail = line[0]
		#print 'tail is %s'%tail
		for item in line[1:]:
			point = item.split(',')[0]
			#print 'point is %s'%point
			distance = item.split(',')[1]
			G.addEdge(tail,point,distance)

	for v in G:
		for w in v.getConnections():
			print w.getId() +' '+ v.getId()

	return G

def main():
	G = loadGraph()


if __name__ == '__main__':
    start = time.time()
    print main()
    print time.time() - start

