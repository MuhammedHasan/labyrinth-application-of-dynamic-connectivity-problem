class QuickUnion(object):
    def __init__(self,size):
        self.connection_map = range(size * size)
        self.size_of_root = [1] * size * size

    def is_connected(self,i,j):
        return self.__root(i) == self.__root(j)

    def connect(self,i,j):
        root_i = self.__root(i)
        root_j = self.__root(j)
        if self.size_of_root[root_i] > self.size_of_root[root_j]:
            self.connection_map[root_i] = root_j
            self.size_of_root[root_j] += root_i
        else:
            self.connection_map[root_j] = root_i
            self.size_of_root[root_i] += root_j

    def __root(self,i):
        while self.connection_map[i] != i:
            self.connection_map[i] = self.connection_map[self.connection_map[i]]
            i = self.connection_map[i]
        return i
