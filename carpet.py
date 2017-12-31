import numpy as np
import scipy.misc
from matplotlib import pyplot as plt

# Generate a spierpinski carpet of variable size and levels


# number of recursive levels, the x and y starting point, x and y end point, and the matrix to paint.
def rec(level, xs, ys,xe, ye, matrix):
    stx = xs/(xe-xs)# "normalized" to help find the center square  
    sty = ys/(ye-ys)  
    if(level == 1): # bottom out
        return
     
    elif(stx % 3 == 1 and sty % 3 ==1): # fill in squares then return
        for i in range(xs, xe):
            for k in range(ys, ye):
                matrix[i][k] = 1  #fill in.
        return
        
    else: # split square into 9 sub-squares and recur more
        step = int((xe-xs)/3) # how large the square is
        for i in range(xs, xe, step):
            for k in range(ys, ye, step):
                rec(level-1, i, k, i+step, k+step, matrix) #hope this works     
    return
    
    
def main():
    levels = 9
    size = 3**8
    matrix = np.zeros([size,size])
    rec(levels, 0, 0,size, size, matrix)
    plt.imshow(matrix)
    plt.show()
#    plt.savefig('carpet.png')
    scipy.misc.imsave('sierpinski_carpet_big-'+str(levels-2)+'.png', matrix)


main()
