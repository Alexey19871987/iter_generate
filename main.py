nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]


class MyRange:
    def __init__(self, l_list):
        self.l_list = l_list

    def __iter__(self):
        self.index_1_level = -1
        self.index_2_level = 0
        return self

    def __next__(self):
        self.index_1_level += 1
        if self.index_1_level == len(self.l_list[self.index_2_level]):
            self.index_2_level += 1
            self.index_1_level = 0
        if self.index_2_level == len(self.l_list):
            raise StopIteration
        return self.l_list[self.index_2_level][self.index_1_level]


def flat_generator(l_list):
    for list_ in l_list:
        for part in list_:
            yield part


if __name__ == '__main__':
    result_list = [item for item in MyRange(nested_list)]
    for item in flat_generator(nested_list):
        print(item)

