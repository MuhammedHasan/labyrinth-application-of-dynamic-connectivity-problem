from random import getrandbits
from QuickFind import QuickFind

class labyrinth(QuickFind):
    def __init__(self):
        QuickFind.__init__(self)
        self.points = self.generate_labyrinth()
        self.up_virtual_point = len(self.points)
        self.down_virtual_point = len(self.points) + 1
        self.__init_connections()
 
    def generate_labyrinth(self):
        points = []
        for i in range(100):
            points.append(getrandbits(1))
        return points

    def __str__(self):
        row_number = 0
        labyrinth_as_string = ' 0123456789\n0'
        for i in range(0,len(self.points)): 
            if self.points[i] == 1:
                labyrinth_as_string += 'x'
            else:
                labyrinth_as_string += ' '
            if (i + 1) % 10 == 0 and row_number != 9:
                labyrinth_as_string += '\n'
                row_number += 1
                labyrinth_as_string += str(row_number)
        return labyrinth_as_string

    def open_wall(self,x,y):
         index = self.__index_from_coordinate(x,y)
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

    def __index_from_coordinate(self,x,y):
        return y * 10 + x


    def __sides_of_point(self,index):
        sides = []
        if index > 9: sides.append(index - 10) #up side
        if (index + 1) % 10 != 0: sides.append(index + 1) #right side
        if index < 89: sides.append(index + 10) #down side
        if index % 10 != 0: sides.append(index - 1) #right side
        return sides


    def is_connected(self, x1, y1,x2,y2):
        i = self.__index_from_coordinate(x1,y1)
        j = self.__index_from_coordinate(x2,y2)
        return super(labyrinth, self).is_connected(i, j)

    def check_percolation(self):
        self.__create_up_virtual_point()
        self.__create_down_virtual_point()
        percolation = super(labyrinth, self).is_connected(self.up_virtual_point, self.down_virtual_point)
        self.__delete_virtual_points()
        return percolation
    
    def __create_up_virtual_point(self):
        self.connection_map.append(self.up_virtual_point)
        for i in range(10):
            if self.points[i] != 1: #if it is not wall
                    self.connect(self.up_virtual_point,i)

    def __create_down_virtual_point(self):
        self.connection_map.append(self.down_virtual_point)
        for i in range(90,100):
            if self.points[i] != 1: #if it is not wall
                    self.connect(self.down_virtual_point,i)

    def __delete_virtual_points(self):
        self.connection_map.pop(self.down_virtual_point)
        self.connection_map.pop(self.up_virtual_point)
        self.__init_connections