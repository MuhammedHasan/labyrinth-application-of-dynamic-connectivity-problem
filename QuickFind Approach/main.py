#-*- coding: cp1254 -*
from labyrinth import labyrinth
from QuickFind import QuickFind

print 'Welcome our labyrinth'
labirent = labyrinth()
print labirent
while True:
    print'''---------Menu---------
1-Generate new labirent
2-Open wall
3-Check there is a connection between two point
4-Check percolation
5-Exit
'''
    selection =0
    try:
        selection = input('->')
    except:
        print'Select between 1-5'
        continue

    if selection == 1:
        labirent = labyrinth()
        print labirent
    
    elif selection == 2:
        x = input('x ->')
        y = input('y ->')
        labirent.open_wall(x,y)
        print labirent 

    elif selection == 3:
        x1 = input('x1 ->')
        y1 = input('y1 ->') 
        x2 = input('x2 ->')
        y2 = input('y2 ->')
        print labirent.is_connected(x1,y1,x2,y2)
    elif selection == 4:
        print labirent.check_percolation()
    
    elif selection == 5:
        break
    
    else:
        print'Select between 1-5' 