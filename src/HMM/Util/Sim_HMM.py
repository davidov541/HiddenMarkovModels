'''
Created on Dec 18, 2009

@author: David McGinnis
'''

from random import random
from ProbUtil import GenerateCDF

def simulate_HMM(Pi, A, B, T, rep):
    PiCDF = GenerateCDF(Pi)
    ACDF = []
    Output = []
    States = []
    BCDF = []
    for i in range(0, len(A)):
        ACDF.append(GenerateCDF(A[i]))
        BCDF.append(GenerateCDF(B[i]))
    for i in range(0, rep):
        CurrState = evalCDF(PiCDF)
        CurrQ = [CurrState]
        CurrO = [evalCDF(BCDF[CurrState])]
        for i in range(0, T):
            CurrCDF = ACDF[CurrState]
            CurrState = evalCDF(CurrCDF)
            CurrO.append(evalCDF(BCDF[CurrState]))
            CurrQ.append(CurrState)
            
        States.append(CurrQ)
        Output.append(CurrO)
    return [States, Output]
            
def evalCDF(CDF):
    num = random()
    for i in range(0, len(CDF)):
        if CDF[i] > num:
            return i
