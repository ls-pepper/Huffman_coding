import argparse
from heap import Heap


def parse_user_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Path and file name for encoder')
    parser.add_argument('output', help='Path and file name for outputting encoding result')
    return parser.parse_args()


class HuffmanEncode:

    def __init__(self, file_path, output_file_path):
        self.file_path = file_path
        self.output_file_path = output_file_path
        self.heap = Heap(attribute='weight')
        self.sym_freq = self.create_dict_symbol_freq()
        self.create_list_nodes()
        self.tree = self.create_tree_huffman()
        self.tree_str = ''
        self.table_dict = self.create_huffman_code_table(self.tree[0])
        self.record_results()

    def create_dict_symbol_freq(self):
        dict_sym_freq = {}
        with open(self.file_path) as f:
            for sym in f.read():
                dict_sym_freq[sym] = dict_sym_freq.get(sym, 0) + 1
        return dict_sym_freq

    class Node:
        def __init__(self, weight, value=None, left=None, right=None, code=None):
            self.value = value
            self.weight = weight
            self.left = left
            self.right = right
            self.code = code

    def create_list_nodes(self):
        for i in self.sym_freq.items():
            self.heap.insert(self.Node(weight=i[1], value=i[0], code='0'))
        return self.heap.data

    def get_min_in_list(self):
        return self.heap.extract_min()

    def create_tree_huffman(self):
        for _ in range(len(self.heap.data) - 1):
            el_1, el_2 = self.get_min_in_list(), self.get_min_in_list()
            el_1.code, el_2.code = '0', '1'
            self.heap.insert(self.Node(left=el_1, right=el_2, weight=el_1.weight + el_2.weight))
        return self.heap.data

    def create_huffman_code_table(self, node):
        if isinstance(node.value, str):
            table_dict = {node.value: {'code': node.code}}
            self.tree_str += str(node.code)
        else:
            self.tree_str += '' if node.code is None else str(node.code)
            table_dict = self.create_huffman_code_table(node.left)
            table_dict.update(self.create_huffman_code_table(node.right))
            for el in table_dict:
                table_dict[el]['code'] = (node.code or '') + table_dict[el]['code']
        return table_dict

    def record_results(self):
        with open(self.file_path) as f:
            code_huffman = ''.join(self.table_dict[i]['code'] for i in f.read())
        str_sym_thee = ''.join(i for i in self.table_dict)
        with open(self.output_file_path, 'w') as f:
            f.write('  '.join([self.tree_str, str_sym_thee, code_huffman]))
        print('Encoding completed!')


if __name__ == '__main__':
    args = parse_user_argument()
    result = HuffmanEncode(args.input, args.output)

