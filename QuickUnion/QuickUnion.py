class QuickUnion(object):
    def __init__(self,size):
        self.connection_map = range(size * size)

    def is_connected(self,i,j):
        return self.__root(i) == self.__root(j)

    def connect(self,i,j):
        root_i = self.__root(i)
        root_j = self.__root(j)
        self.connection_map[root_i] = root_j


    def __root(self,i):
        while self.connection_map[i] != i:
            i = self.connection_map[i]
        return i
