class QuickFind(object):
    def __init__(self):
        self.connection_map = range(100)

    def is_connected(self,i,j):
        return self.connection_map[i] == self.connection_map[j]

    def connect(self,i,j):
        len_of_map = len(self.connection_map)
        id_that_connected = self.connection_map[i]
        for item in range(len_of_map):
            if(self.connection_map[item] == id_that_connected):
                self.connection_map[item] = self.connection_map[j]