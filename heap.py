class Heap:
    def __init__(self, attribute=None, data=None):
        self.data = data or []
        self.attribute = attribute
        self.size = len(self.data)

    def sift_up(self, obj_index):
        if obj_index > 0 and (self.data[(obj_index - 1) // 2].__dict__[self.attribute] >
                              self.data[obj_index].__dict__[self.attribute]):
            self.data[obj_index], self.data[(obj_index - 1) // 2] = \
                self.data[(obj_index - 1) // 2], self.data[obj_index]
            self.sift_up((obj_index - 1) // 2)

    def sift_down(self, obj_index):
        if 2 * obj_index + 1 <= self.size - 1:
            new_obj_index = obj_index
            if self.data[2 * obj_index + 1].__dict__[self.attribute] < \
                    self.data[new_obj_index].__dict__[self.attribute]:
                new_obj_index = 2 * obj_index + 1
            if 2 * obj_index + 2 <= self.size - 1 and \
                    self.data[2 * obj_index + 2].__dict__[self.attribute] < \
                    self.data[new_obj_index].__dict__[self.attribute]:
                new_obj_index = 2 * obj_index + 2
            if new_obj_index == obj_index:
                return
            self.data[obj_index], self.data[new_obj_index] = self.data[new_obj_index], self.data[obj_index]
            self.sift_down(new_obj_index)

    def insert(self, obj):
        self.data.append(obj)
        self.size += 1
        self.sift_up(self.size - 1)

    def extract_min(self):
        min_obj = self.data[0]
        if self.size != 1:
            self.data[0] = self.data.pop()
            self.size -= 1
            self.sift_down(0)
        else:
            self.data.pop()
            self.size -= 1
        return min_obj


if __name__ == '__main__':
    ...
