'''
Created on Dec 18, 2009

@author: David McGinnis
'''

def GenerateCDF(arr):
    total = 0.0
    result = []
    for i in range(0, len(arr)):
        total += arr[i]
        result.append(total)
    return result