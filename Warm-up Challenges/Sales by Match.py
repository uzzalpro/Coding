#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    # return sum(num//2 for num in Counter(ar).values())    
    
    my_list=sorted(ar)
    duplicates=[]
    # number_of_item = 0
    pair=[]
    for i in my_list:
        if my_list.count(i)>1:
            if i not in duplicates:
                duplicates.append(i)
                pair.append(ar.count(i)//2)
    return sum(pair)
                    
        # else:
    # return len(duplicates)
    # number_of_item= max(duplicates)
    # pair = ar.count(number_of_item)
    # if pair % 2 == 0:
    #     return pair
    # else:
    #     return pair-1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
