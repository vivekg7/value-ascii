#import pyautogui as pg
import numpy as np
import cv2
#import time

# ------------------------------------------------------------------------
#                     Global Variables
# ------------------------------------------------------------------------

# Terminal screen dimensions
tw = 240
th = 120

pairs = [[' ', 0], ['`', 5], ["'", 8], ['.', 8], ['-', 9], [',', 13], [':', 13], ['_', 13], ['~', 14], ['"', 17], ['+', 17], ['^', 18], ['!', 20], [';', 20], ['=', 20], ['*', 23], ['<', 25], ['>', 25], ['|', 25], ['/', 26], ['\\', 26], ['?', 28], ['(', 30], [')', 30], ['c', 30], ['l', 30], ['7', 31], ['L', 32], ['i', 32], ['t', 32], ['v', 32], ['r', 34], [']', 35], ['f', 35], ['s', 35], ['z', 35], ['}', 35], ['J', 36], ['T', 36], ['[', 36], ['x', 36], ['{', 36], ['1', 37], ['4', 37], ['C', 38], ['Y', 38], ['j', 38], ['F', 39], ['n', 39], ['u', 39], ['2', 40], ['3', 40], ['I', 40], ['o', 40], ['a', 41], ['e', 41], ['5', 43], ['V', 43], ['y', 43], ['Z', 44], ['h', 44], ['k', 45], ['E', 46], ['S', 47], ['9', 48], ['X', 48], ['6', 49], ['P', 49], ['&', 50], ['b', 50], ['d', 50], ['U', 51], ['A', 52], ['G', 52], ['O', 52], ['m', 52], ['w', 52], ['K', 53], ['p', 53], ['q', 53], ['#', 54], ['0', 54], ['H', 55], ['8', 57], ['D', 57], ['R', 59], ['%', 60], ['Q', 60], ['B', 63], ['N', 64], ['$', 65], ['g', 65], ['@', 70], ['M', 73], ['W', 73]]

lenp = len(pairs)

# ------------------------------------------------------------------------
#                     Util Functions
# ------------------------------------------------------------------------

def binarySearch(val, p, r):
    if p >= r:
        return r
    q = int((p+r)/2)
    if pairs[q][1] > val:
        return binarySearch(val, p, q-1)
    if pairs[r][1] <= val:
        return r
    if q+1 == r:
        return q
    return binarySearch(val, q, r)

def getChar(val):
    pos = binarySearch(val, 0, lenp-1)
    #print('BinarySearch for ', val, 'Resulted with ', pairs[pos])
    if pos == lenp-1:
        return pairs[pos][0]
    diff1 = abs(pairs[pos][1] - val)
    diff2 = abs(pairs[pos+1][1] - val)
    if diff1 < diff2:
        return pairs[pos][0]
    return pairs[pos+1][0]

def mapp(val):
    return int(val*(75/255))

# from 0-255 to 0-75 for all pixels
def mapImg(im):
    pass

# ------------------------------------------------------------------------
#                     Main Driver Function
# ------------------------------------------------------------------------
if __name__ == "__main__":
    filename = input('Enter filename: ')
    im = cv2.imread(filename, 0)          # Grayscale
    im = cv2.resize(im, (tw, th*2))
    print(im.shape)
    #cv2.imshow('Image', im)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    for y in range(th):
        #print(y, end=": ")
        for x in range(tw):
            pix = int(im[2*y][x])
            pix += im[1+2*y][x]
            #print(pix, end=" ")
            print(getChar(mapp(pix/2)), end="")
        print()
    #print(lenp)
    #for i in range(75):
    #    print('Binary Search for ', i, ' Resulted with ', pairs[binarySearch(i, 0, lenp-1)])
