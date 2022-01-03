#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    n = len(word)
    height_word = word[0]
    a_z_index = 'abcdefghijklmnopqrstuvwxyz'
    value_of_a_z_index = 0
    value_of_h = h[0] 
    
    for i in word:
        if i > height_word:
            height_word = i
            
    if height_word in a_z_index:
        value_of_a_z_index = a_z_index.find(height_word)
    
    # value_of_h = h[value_of_a_z_index]
    for j in h[:value_of_a_z_index+1]:
        if j > value_of_h:
            value_of_h = j
        
    return value_of_h * n     
            
    
    
    
    # if "z" in word:
    #     for i in h:
    #         if i > height:
    #             height = i
    # if "z" not in word:
    #     for i in h[0:n]:
    #         if i > height:
    #             height = i
    # return height*n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
