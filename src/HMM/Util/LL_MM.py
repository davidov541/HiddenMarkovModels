'''
Created on Dec 17, 2009

@author: David McGinnis
'''

from math import log

""" 
Gets the log-likelihood of the given output
for the given Markov Model defined by Pi and A.
This assumes that Q contains values which match
up to the index of A. Because of the ability to
index according to strings in Python, this 
shouldn't be an issue.
Also, A is assumed to be such that A[oldState][newState]
denotes the probability of moving from the oldState
to the newState.
"""
def LL_MM(Pi, A, Q):
    startP = Pi[Q[0]]
    score = findScore(Q, A, startP, 0)
    return score

"""
Helper function for LL_MM which computes the probability
of a given output given the Markov Model. Uses simple
recursion in order to do this.
"""
def findScore(Q, A, P, i):
    if(len(Q) - 1 == i):
        return P
    else:
        NextProb = A[Q[i]][Q[i + 1]]
        return findScore(Q, A, P * NextProb, i + 1)