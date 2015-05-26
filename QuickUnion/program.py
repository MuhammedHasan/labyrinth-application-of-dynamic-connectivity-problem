from labyrinth import labyrinth

class program(object):
    def __init__(self):
        self.is_labyrinth_generated = False
        print 'Welcome our labyrinth'

    def mainloop(self):
        while True:
            print'''---------Menu---------
1-Generate new labyrinth
2-Open wall
3-Check there is a connection between two point
4-Check percolation
5-Exit'''
            selection = self.__input_selection()
            if selection == 1:
                labirent = self.__create_labyrinth()
                print labirent
            elif selection == 2 and self.__is_labyrinth_generated():
                coordinates = self.__input_point(1)
                try:
                    labirent.open_wall(coordinates[0],coordinates[1])
                except:
                    print 'please select valide coordinate'
                print labirent 
            elif selection == 3 and self.__is_labyrinth_generated():
                try:
                    coordinates = self.__input_point(2)
                    print labirent.is_connected(coordinates[0],coordinates[1],coordinates[2],coordinates[3])
                except:
                    print 'please select valide coordinate'
            elif selection == 4 and self.__is_labyrinth_generated():
                print labirent.check_percolation()
            elif selection == 5:
                break

    def __input_selection(self):
        selection = 0
        correct_input = False
        while not correct_input:
            try:
                selection = input('->')
                if selection > 5 or selection < 0:
                    print 'Select between 1-5'
                    continue
                correct_input = True
            except:
                print 'Select between 1-5'
        return selection

    def __input_size(self):
        size = 0
        correct_input = False
        while not correct_input:
            try:
                size = input('Size of labyrinth ->')
                correct_input = True
            except:
                print 'Select between 1-36'
        return size

    def __input_point(self, numberOfPoint):
        correct_input = False
        while not correct_input:
            coordinates = list()
            try:
                if numberOfPoint == 1:
                    coordinates.append(raw_input('x ->'))
                    coordinates.append(raw_input('y ->'))
                elif numberOfPoint > 1:
                    for i in range(1,numberOfPoint + 1):
                        coordinates.append(raw_input('x'+str(i)+' ->'))
                        coordinates.append(raw_input('y'+str(i)+' ->'))
                correct_input = True
            except:
                print 'please select valide coordinate input'
        return coordinates

    def __is_labyrinth_generated(self):
        if self.is_labyrinth_generated:
            return True
        else:
            print 'first generate labyrinth'
            return False

    def __create_labyrinth(self):
        correct_input = False
        size = self.__input_size()
        while not correct_input:
            try:
                labirent = labyrinth(size)
                correct_input = True
            except:
                print 'Please write size between 1-36'
                size = self.__input_size()
        self.is_labyrinth_generated = True
        return labirent

