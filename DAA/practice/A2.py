class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def nodes(self):
        return(self.left, self.right)

    def children(self):
        return(self.left, self.right)


def huffman_func(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    d = dict()
    (l, r) = node.children()
    d.update(huffman_func(l, True, binString+'0'))
    d.update(huffman_func(r, True, binString+'1'))
    return d


string = input("Enter a string: ")
print()

freq = {}
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]

    node = NodeTree(key1, key2)

    nodes.append((node, c1+c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_func(nodes[0][0])

print(huffmanCode)

for (char, frequency) in freq:
    print('%-4r | %12s' % (char, huffmanCode[char]))
