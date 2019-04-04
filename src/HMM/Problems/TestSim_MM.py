'''
Created on Dec 18, 2009

@author: mcginnda
'''

from Util import Sim_MM
from Util import PrintUtil

if __name__ == '__main__':
    A = [[0.8, 0.1, 0.1], [0.3, 0.2, 0.5], [0.2, 0.6, 0.2]]
    Pi = [0.6, 0.2, 0.2]
    T = 5
    rep = 10
    outputs = Sim_MM.simulate_MM(Pi, A, T, rep)
    PrintUtil.PrintOutputs(outputs)