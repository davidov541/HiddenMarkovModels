'''
Created on Dec 18, 2009

@author: David McGinnis
'''

import PrintUtil

def train_HMM(N, M, Q, O):
    Pi = []
    A = []
    B = []
    sum = []
    
    # Initialize variables
    for i in range(0, N):
        sum.append(0.0)
        Pi.append(0.0)
        for i in range(0, N):
            A.append([])
            B.append([])
            for j in range(0, N):
                A[i].append(0.0)
            for j in range(0, M):
                B[i].append(0.0)
        
    # Get initial counts
    for rep in range(0, len(Q)):
        Pi[Q[rep][0]] += 1.0
        B[Q[rep][0]][O[rep][0]] += 1.0
        for i in range(0, len(Q) - 1):
            A[Q[rep][i]][Q[rep][i + 1]] += 1.0
            B[Q[rep][0]][O[rep][0]] += 1.0
            sum[Q[rep][i]] += 1.0
            
    # Get probabilities from counts
    for i in range(0, N):
        for j in range(0, N):
            A[i][j] = A[i][j] / sum[i]
            B[i][j] = B[i][j] / sum[i]
                
    lamb = [Pi, A, B]
    return lamb