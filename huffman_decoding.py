import argparse


def parse_user_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Path and file name for decoding')
    parser.add_argument('output', help='Path and file name for outputting decoding result')
    return parser.parse_args()


class DecodeHuffman:

    def __init__(self, encoded_file_path, decoded_file_path):
        self.encoded_file_path = encoded_file_path
        self.decoded_file_path = decoded_file_path
        self.tree_str, self.symbol_freq_list, self.encoded_str = self.read_from_file()
        self.tree_dict = self.get_tree_dict(self.tree_str, self.symbol_freq_list)[1]
        self.decoding()

    def read_from_file(self):
        symbol_freq_list = []
        with open(self.encoded_file_path) as f:
            file_data = f.read().split('  ')
            for sym in file_data[1]:
                symbol_freq_list.append(sym)
            tree_str = file_data[0]
            encoded_str = file_data[2]
        return tree_str, symbol_freq_list, encoded_str

    def get_tree_dict(self, tree_str, symbol_freq_list, code='', ind=0, tree_dict={}):
        for _ in range(2):
            code += tree_str[ind]
            ind += 1
            if ind < len(tree_str) and tree_str[ind] == '0':
                ind = self.get_tree_dict(tree_str, symbol_freq_list, code, ind, tree_dict)[0]
            else:
                tree_dict[code] = symbol_freq_list.pop(-len(symbol_freq_list))
            code = code[:-1]
        return ind, tree_dict

    def decoding(self):
        sequence = ''
        with open(self.decoded_file_path, 'w') as f:
            for sym in self.encoded_str:
                sequence += sym
                if sequence in self.tree_dict:
                    f.write(self.tree_dict[sequence])
                    sequence = ''
        print('Decoding completed!')


if __name__ == '__main__':
    args = parse_user_argument()
    result = DecodeHuffman(args.input, args.output)

