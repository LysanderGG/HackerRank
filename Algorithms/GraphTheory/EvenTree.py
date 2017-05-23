class Node:
    def __init__(self, id, parent=None):
        self.id = id
        self.children = []
        self.parent = parent
        self.weight = 1
    
    def add_child(self, child):
        self.children.append(child)
        
    def update_weight(self):
        self.weight = 1
        for child in self.children:
            child.update_weight()
            self.weight += child.weight
            
    def __repr__(self):
        return "id: {} weight: {}".format(self.id, self.weight)
        

m, n = input().strip().split(' ')
m, n = int(m), int(n)
nodes = {1: Node(1)}

for _ in range(1, m):
    a, b = input().strip().split(' ')
    a, b = int(a), int(b)
    
    if a not in nodes:
        nodes[a] = Node(id=a, parent=nodes[b])
        nodes[b].add_child(nodes[a])
    elif b not in nodes:
        nodes[b] = Node(id=b, parent=nodes[a])
        nodes[a].add_child(nodes[b])
    else:
        assert(0)

nodes[1].update_weight()        
del nodes[1]
#print(nodes)
nb_even_weighted_nodes = sum((node.weight % 2 == 0 for _, node in nodes.items()))
print(nb_even_weighted_nodes)
