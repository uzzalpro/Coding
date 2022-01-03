#!/bin/python3
'''

When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with 
a blue rectangle.In this PDF viewer, each word is highlighted independently. For example:

There is a list of  26 character heights aligned by index to their letters. 
For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. 
Using the letter heights given, determine the area of the rectangle highlight in (mm^2) 
assuming all letters are (1mm) wide.

h = [1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,5,5,2,5,5,5,5,5,7] word = 'tron'

The heights are t=2, o=1,r=1 and n=1. The tallest letter is 2 high and there are 2 letters. 
The hightlighted area will be 2*4 = 8mm^2 so the answer is 8.

Constraints:
1 <= h[?], <= 7 where ? is an English lowercase letter.
word contains no more than 10 letters.

-----------------------
Sample Input 0

1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc
Sample Output 0

9
Explanation 0

We are highlighting the word abc:

Letter heights are a = 1,b=3 and c=1. The tallest letter, b, is 3mm high. The selection area for this word is 3. 
1mm.3mm=9mm^2

Note: Recall that the width of each character is 1mm.
--------------------------------
Sample Input 1

1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba
Sample Output 1

28
Explanation 1

The tallest letter in zaba is z at 7mm. The selection area for this word is 4*1mm*7mm=28mm^2.







'''

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
