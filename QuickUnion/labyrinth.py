from random import getrandbits
from QuickUnion import QuickUnion
from coordinateSystem import coordinateSystem

class labyrinth(QuickUnion, coordinateSystem):
    def __init__(self, size):
        coordinateSystem.__init__(self,size)
        QuickUnion.__init__(self,size)
        self.points = self.generate_labyrinth(size)
        self.up_virtual_point = size * size
        self.down_virtual_point = size * size + 1
        self.__init_connections()
 
    def generate_labyrinth(self,size):
        points = []
        for i in range(size * size):
            points.append(getrandbits(1))
        return points

    def __str__(self):
        points = map(lambda x:'x' if x == 1 else ' ',self.points)  
        return self.draw_coordinate_system(points)

    def open_wall(self,x,y):
        index = self.index_from_coordinate(x,y)
        if self.points[index] == 1: 
            self.points[index] = 0
            self.__connect_point_with_sides(index)
        else:
            print 'Error: There is not wall in there'

    def __init_connections(self):
        len_of_points = len(self.points)
        for index in range(len_of_points):
            if self.points[index] == 1: #if it is wall countinue
                continue
            else:
                self.__connect_point_with_sides(index)

    def __connect_point_with_sides(self,index):
        sides = self.__sides_of_point(index)
        for side in sides: 
                if self.points[side] != 1: #if it is not wall
                    self.connect(index,side)

    def __sides_of_point(self,index):
        sides = []
        if index > self.size - 1 : sides.append(index - self.size) #up side
        if (index + 1) % self.size != 0: sides.append(index + 1) #right side
        if index < (self.size * self.size) - self.size - 1 : sides.append(index + self.size) #down side
        if index % self.size != 0: sides.append(index - 1) #left side
        return sides


    def is_connected(self, x1, y1,x2,y2):
        i = self.index_from_coordinate(x1,y1)
        j = self.index_from_coordinate(x2,y2)
        return super(labyrinth, self).is_connected(i, j)

    def check_percolation(self):
        self.__create_up_virtual_point()
        self.__create_down_virtual_point()
        percolation = super(labyrinth, self).is_connected(self.up_virtual_point, self.down_virtual_point)
        self.__delete_virtual_points()
        return percolation
    
    def __create_up_virtual_point(self):
        self.connection_map.append(self.up_virtual_point)
        for i in range(self.size):
            if self.points[i] != 1: #if it is not wall
                    self.connect(self.up_virtual_point,i)

    def __create_down_virtual_point(self):
        self.connection_map.append(self.down_virtual_point)
        for i in range(self.size * (self.size - 1), (self.size * self.size)):
            if self.points[i] != 1: #if it is not wall
                    self.connect(self.down_virtual_point,i)

    def __delete_virtual_points(self):
        self.connection_map.pop(self.down_virtual_point)
        self.connection_map.pop(self.up_virtual_point)
        self.__init_connections