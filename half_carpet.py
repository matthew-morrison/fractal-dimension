import numpy as np
from matplotlib import pyplot as plt

# generate something like a sierpinski carpet, but with triangles.


# number of recursive levels, the x and y starting point, x and y end point, and the matrix to paint.
def rec(level, xs, ys,xe, ye, matrix):
    stx = xs/(xe-xs)
    sty = ys/(ye-ys)  # "normalized" to help find the center triangle  
    if(level == 1): # bottom out
        return
     
    elif(stx % 3 == 1 and sty % 3 ==1): # fill in squares then return
        
        for i in range(xs, xe):
            for k in range(ys, ye):
                #if(i>= xs+k-ys or i <= xe-k+ys):
                #    print(i>= xs+k, i <= xe-k)
                
                if(i-xs >= k-ys or i-xs <= ye-k-ys): #why does the or work?
                    print('filled', i-xs, k-ys, 'layer', level)
                    matrix[i][k] = 1  #fill in.
        return
        
    else: # split square into 9 sub-squares and recur more
        step = int((xe-xs)/3) # how large the square is
        for i in range(xs, xe, step):
            for k in range(ys, ye, step):
                rec(level-1, i, k, i+step, k+step, matrix) #hope this works     
    return
    
    
    
def main():
    levels = 6
    size = 3**7
    matrix = np.zeros([size,size])
    rec(levels, 0, 0,size, size, matrix)
    plt.imshow(matrix)
    plt.show()



main()
