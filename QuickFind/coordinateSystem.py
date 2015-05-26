class coordinateSystem(object):

    def __init__(self, size=0):
        self.size = 0
        self.set_size(size)
        self.values_coordinates = '0123456789abcdefghijklmnopqrstuvwxyz'
        self.coordinates = list(self.values_coordinates)[:size]

    def set_size(self,size):
        if size > 36:
            raise Exception('Coordinate system size cannot be more than 36')
        else:
            self.size = size


    def draw_coordinate_system(self , values):
        system = ' '
        for i in self.coordinates:
            system += str(i)
        system +=  '\n' 
        for i in range(self.size):
            system += str(self.coordinates[i]) + ''.join(map(str,values[i * self.size : (i + 1) * self.size])) + '\n'
        return system

    def index_from_coordinate(self, x, y):
        x_value = self.coordinates.index(x)
        y_values = self.coordinates.index(y)
        return (y_values * self.size) + x_value


        


