from math import *
from time import sleep
def genPoints():
    
    y_points = {}
    z_points = {}

    ## Get our y points ##
    print '\nY Points\n|y y^2|\n--------'
    for i in range(0,mod):
        sqr = (i*i) % mod
        y_points[i] = sqr
        print str(i) + ' ' + str(sqr)
    
    ## Get our z points ##
    print '\nXZ Points\n|x z Square?|\n--------'
    for i in range(0,mod):
        z = (i**3 + x*i + const) % mod
        #print str(i) + ' ' + str(z)
        if z in y_points.values():
            print str(i) + ' ' + str(z) + " yes"
            z_points[i] = z

    sleep(1)
    
    ## Get our points ##
    for ax, ay in z_points.iteritems():
        for bx, by in y_points.iteritems():
            if ay == by:
                print '(',ax, ",", bx, ')'

if __name__ == '__main__':
    x = input('Enter x Term: ')
    const = input('Enter c Term: ')
    mod = input('Enter mod Term: ')
    genPoints()
