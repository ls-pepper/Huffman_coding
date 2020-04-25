
tree_str = ''
sym_freq=[]
encoding_str = ''
with open('2.txt') as f:
    file_data = f.read().split('  ')
    for sym in file_data[1]:
        sym_freq.append(sym)
    tree_str = file_data[0]
    encoding_str = file_data[2]

# tree_dict = {}
def getTreeDict(tree,syms,code='',ind = 0,tree_dict = {}):
    for _ in range(2):
        code += tree[ind]
        ind += 1
        if ind < len(tree) and tree[ind] == '0':
            ind = getTreeDict(tree, syms, code, ind, tree_dict)[0]
        else:
            tree_dict[code] = syms.pop(-len(syms))
        code = code[:-1]
    return ind, tree_dict

def decode(dict,encoding_str):
    sequnce = ''
    decode_str = ''
    for sym in encoding_str:
        sequnce += sym
        if sequnce in dict:
            decode_str += dict[sequnce]
            sequnce = ''
    return decode_str

# qwe = getTreeDict(tree_str,sym_freq)[1]
# print(tree_dict)
a = decode(getTreeDict(tree_str,sym_freq)[1],encoding_str)
print(a)



