# Write a program to implement Huffman Encoding using a greedy strategy.

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    # def __str__(self):
    #     return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


string = input("Enter string for huffman encoding ")
# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    # select min freq any 2 nodes (the list is already sorted in reverse order)
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    # this is stored at indexes like this:
    # index: -2      -1
    # nodes: key2   key1

    nodes = nodes[:-2]
    # takes the nodes yet to be used for min heap

    node = NodeTree(key1, key2)

    nodes.append((node, c1 + c2))
    # this line adds the node with sum of the 2 min freq nodes as the freq to the nodes dict

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])
# calls the main huffman tree function with the root node

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))
