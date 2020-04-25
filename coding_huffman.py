sym_freq = {}
with open('1.txt') as f:
    for sym in f.read():
        sym_freq[sym] = sym_freq.get(sym, 0) + 1


class Node:
    def __init__(self, weight, value=None, left=None, right=None, code=None):
        self.value = value
        self.weight = weight
        self.left = left
        self.right = right
        self.code = code


nodes = [Node(weight=i[1], value=i[0], code='0') for i in sym_freq.items()]


def getMinInList(list_nodes):
    list_nodes.sort(key=lambda x: x.weight, reverse=True)
    return list_nodes.pop()


for _ in range(len(nodes) - 1):
    el_1, el_2 = getMinInList(nodes), getMinInList(nodes)
    el_1.code, el_2.code = '0', '1'
    nodes.append(Node(left=el_1, right=el_2, weight=el_1.weight + el_2.weight))

thee_str = ''


def createCodeDict(Node):
    global thee_str
    if isinstance(Node.value, str):
        retDic = {Node.value: {'code': Node.code}}
        thee_str += str(Node.code)
    else:
        thee_str += '' if Node.code == None else str(Node.code)
        retDic = createCodeDict(Node.left)
        retDic.update(createCodeDict(Node.right))
        for el in retDic:
            retDic[el]['code'] = (Node.code or '') + retDic[el]['code']
    return retDic


dict_out = createCodeDict(nodes[0])

with open('1.txt') as f:
    out_code = ''.join(dict_out[i]['code'] for i in f.read())

for k in dict_out:
    print(k + ': ' + dict_out[k]['code'])

str_sym_thee = ''.join(i for i in dict_out)

print(thee_str, str_sym_thee, out_code)
print(thee_str)
print(str_sym_thee)
# print(out_code)
with open('2.txt', 'w') as f:
    f.write('  '.join([thee_str, str_sym_thee, out_code]))
