import random
import time


class adjacency(object):
	def __init__(self,node,edge):
		self.node = node
		self.edge = edge
	def contract(self,other):
		self.node = self.node + other.node
		for i in other.edge:
			if i not in self.edge:
				if i not in self.node:
					self.edge.append(i)

#    def __repr__(self):
#        return 'Adjacency(node = %r, edge = %r)' % (self.node, self.edge)


def mincut(graph):
	while len(graph)>2:
		pickNode = random.choice(graph)
		print 'Graph type is %s' % type(graph)
		print 'Node type, is %s' %type(pickNode)
		pickEdge = random.choice(pickNode.edge)
		print 'pickEdge type, %s'%type(pickEdge)
		pickNbr = [i for i in graph if pickEdge in i.node] #difference
		print 'Nbr[0] type is, %s' %type(pickNbr[0])
		pickNode.contract(pickNbr[0])
		graph.remove(pickNbr[0])


	return graph

def main():
    file_in = open('array.txt')
#   data = [[[int(line.split()[0])], [int(i) for i in line.split()[1:]]] for line in file_in]
    data = []
    for line in file_in:
        val = [int(line.split()[0])]
        adj = [int(i) for i in (line.split()[1:])]
        data.append([val,adj])

    #print data
    graph = [adjacency(i[0], i[1]) for i in data]
    #print graph[1].edge
    cut = len(mincut(graph)[0].edge)
    ite = len(graph)**2
    for i in range(ite):
        trial = len(mincut(graph)[0].edge)
        if trial < cut:
            cut = trial
    print 'Mincut is ' + str(cut)
#    for i in graph:
#        print str(i.node) +'->'+ str(i.edge)


if __name__ == '__main__':
    start = time.time()
    main()
    print time.time() - start