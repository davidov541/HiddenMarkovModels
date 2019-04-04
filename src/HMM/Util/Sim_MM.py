'''
Created on Dec 18, 2009

@author: David McGinnis
'''

from random import random
from ProbUtil import GenerateCDF

def simulate_MM(Pi, A, T, rep):
    PiCDF = GenerateCDF(Pi)
    ACDF = []
    Result = []
    for i in range(0, len(A)):
        ACDF.append(GenerateCDF(A[i]))
    for i in range(0, rep):
        CurrState = getState(PiCDF)
        Output = [CurrState]
        for i in range(0, T):
            CurrCDF = ACDF[CurrState]
            CurrState = getState(CurrCDF)
            Output.append(CurrState)
        Result.append(Output)
    return Result
            
def getState(CDF):
    num = random()
    for i in range(0, len(CDF)):
        if CDF[i] > num:
            return i
