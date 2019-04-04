'''
Created on Dec 16, 2009

@author: David McGinnis
'''

from Util.LL_MM import LL_MM
from math import log
from decimal import Decimal

"""
The given files contain coded sequences. One sequence codes a message in English
using the code a=1, b=2, ... etc. The other is gibberish. Which file contains the
coded message?
"""

if __name__ == '__main__':
    # Open file and get output.
    file = open("..\..\Files\mystery1.txt", "r")
    input = file.readline()
    inputs = input.split()
    Q = []
    for i in inputs:
        Q.append(int(i) - 1)
        
    # Set up Markov Models
    A1 = []
    Pi1 = []
    A2i = ["8000", "1600", "3000", "4400", "12000", "2500", "1700", "6400", "8000", "400", "800", "4000", "3000", "8000", "8000", "1700", "500", "6200", "8000", "9000", "3400", "1200", "2000", "400", "2000", "200"]
    A2 = []
    Pi2 = []
    for i in range(0, 26):
        # We are using Decimals in order to allow infinitely (theoretically) small numbers.
        Pi1.append(Decimal("0.03846154")) # 0.03846154 is 1/26 according to Matlab
        Pi2.append(Decimal(A2i[i]) / Decimal("106400"))
        A1.append([])
        A2.append([])
        for j in range(0, 26):
            A1[i].append(Pi1[i])
            A2[i].append(Pi2[i])
            
    # Get scores of each machine and compare.
    score1 = LL_MM(Pi1, A1, Q)
    score2 = LL_MM(Pi2, A2, Q)
    print "Score: %f" % log(score2 / score1, 10)