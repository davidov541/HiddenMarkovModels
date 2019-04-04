'''
Created on Dec 18, 2009

@author: David McGinnis
'''

import PrintUtil

def train_MM(N, Q):
    Pi = []
    A = []
    sum = []
    for i in range(0, N):
        sum.append(0.0)
        if Q[0] == i:
            Pi.append(1)
        else:
            Pi.append(0)
    for i in range(0, N):
        A.append([])
        for j in range(0, N):
            A[i].append(0.0)
    for i in range(0, len(Q) - 1):
        A[Q[i]][Q[i + 1]] += 1.0
        sum[Q[i]] += 1.0
    for i in range(0, N):
        for j in range(0, N):
            A[i][j] = A[i][j] / sum[i]
    lamb = [Pi, A]
    return lamb