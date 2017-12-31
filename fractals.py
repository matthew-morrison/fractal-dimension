import cv2
import sys
import numpy as np
from functools import reduce
from PIL import Image
from math import floor, log, ceil # the whole house
from matplotlib import pyplot as plt



# convert colour image to black and white
def convert_to_blacks(img):
    thresh = cv2.THRESH_BINARY
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img_bw = cv2.threshold(img_gray, 127, 255, thresh)
    return img_bw


# take an even spread of num from a list
#this is definitely not borrowed from stackoverflow
def takespread(sequence, num):
    length = float(len(sequence))
    for i in range(num):
        yield sequence[int(ceil(i * length / num))]


# returns factors of n    
#I definitely borrowed this from stackoverflow
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


# check if box is touching fractal
def check_black(b, i, k, arr):
    thresh = b*b*1
    return arr[i:i+b,k:k+b].sum() > thresh


#supply a blocksize and a matrix to get the hitcount
def hits_with_boxsize(arr, boxsize):
    shape = arr.shape 
    results = np.zeros([ int(shape[0]/boxsize) , int(shape[1]/boxsize) ])
    
    # for each box
    for i in range(0, shape[0], boxsize):
        for k in range(0, shape[1], boxsize):
            box_x = floor(i/boxsize)
            box_y = floor(k/boxsize)
            
            #check inside that box
            if(check_black(boxsize, i, k, arr)):
                results[box_x, box_y] = 1
    hits = results.sum()
    return (hits, results) # why return two results when one is derived from the other?


def main():    
    filename = sys.argv[1]
    img = Image.open(filename).convert('RGB')
    arr = np.array(img, dtype=np.uint8)
    arr_cp = arr
    arr = np.invert(arr, dtype=np.uint8)

    cv2_img = cv2.imread(filename, 0)
    img_bw = convert_to_blacks(arr)

    if(arr.shape[0] != arr.shape[1]):
        print("dimensions aren't square... there will likely be an error")
      
    fact = sorted(factors(len(arr))) # get all factors of image size
    spaced10 = fact[1:len(fact)-1] #remove 1 and n.
    if(len(fact) > 10): # could be lots of factors, only take 10
        spaced10 = list(takespread(spaced10, 10))  # an even distribution to view the fractal at different sizes
    
    hits, box_arr = zip(*list(hits_with_boxsize(arr, i) for i in spaced10)) # get box-counting results
    
    dim = list( (log(hits[i]/hits[i+1], spaced10[i+1]/spaced10[i]) for i in range(len(hits)-1))) # calculate dimension
    print("Fractal dimension measurement taken at different box sizes.")
    print(dim)
    print('It is left as an exercise to the user to determine which one or more dimension (or any) is the correct fractal dimension')
    
    
    # set up plots
   
    f, ax = plt.subplots(3,4)
    ax[0,0].set_title('Original image')
    ax[0,0].imshow(arr_cp, 'gray')
    
    ax[0,1].set_title('Converted image')
    ax[0,1].imshow(img_bw, 'gray')
    
    # crazy looping because fun
    
    counter = 0
    for x in list(zip(*np.ndenumerate(ax)))[1][2:]: #enumerate the 2d arr, split the x,y and n, retrieve as list, then chop off first 2 elements before looping through
        if(counter < len(spaced10)): #because num of subplots may not match amount we are graphing.
            x.set_title('Boxcount size ' + str(spaced10[counter]))
            x.imshow(box_arr[counter], 'gray')
            counter = counter + 1
    

# old loopless way for posterity
    
#    ax[0,2].set_title('Boxcount size '+ str(spaced10[0]))
#    ax[0,2].imshow(box_arr[0], 'gray')
#  
#    ax[0,3].set_title('Boxcount size '+ str(spaced10[1]))
#    ax[0,3].imshow(box_arr[1], 'gray')
#    
#    ax[1,0].set_title('Boxcount size '+str(spaced10[2]))
#    ax[1,0].imshow(box_arr[2], 'gray')
#    
#    ax[1,1].set_title('Boxcount size ' +str(spaced10[3]))
#    ax[1,1].imshow(box_arr[3], 'gray')
#    
#    ax[1,2].set_title('Boxcount size '+ str(spaced10[4]))
#    ax[1,2].imshow(box_arr[4], 'gray')
#    
#    ax[1,3].set_title('Boxcount size '+ str(spaced10[5]))
#    ax[1,3].imshow(box_arr[5], 'gray')
#    
#    ax[2,0].set_title('Boxcount size '+ str(spaced10[6]))
#    ax[2,0].imshow(box_arr[6], 'gray')
#    
#    ax[2,1].set_title('Boxcount size '+ str(spaced10[7]))
#    ax[2,1].imshow(box_arr[7], 'gray')            
#    
#    ax[2,2].set_title('Boxcount size '+ str(spaced10[8]))
#    ax[2,2].imshow(box_arr[8], 'gray')
#    
#    ax[2,3].set_title('Boxcount size '+ str(spaced10[9]))
#    ax[2,3].imshow(box_arr[9], 'gray') 
    
    plt.show()


main()
