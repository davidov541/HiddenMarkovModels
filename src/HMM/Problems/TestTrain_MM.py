'''
Created on Dec 18, 2009

@author: David McGinnis
'''

from HMM.Util import Sim_MM
from HMM.Util import Train_MM
from HMM.Util import PrintUtil

if __name__ == '__main__':
    A = [[0.8, 0.1, 0.1], [0.3, 0.2, 0.5], [0.2, 0.6, 0.2]]
    Pi = [0.6, 0.2, 0.2]
    T = 5000000
    rep = 1
    outputs = Sim_MM.simulate_MM(Pi, A, T, rep)
    PrintUtil.PrintLambda(A, Pi)
    PrintUtil.PrintOutputs(outputs)
    newlamb = Train_MM.train_MM(len(Pi), outputs[0])
    PrintUtil.PrintLambda(newlamb[1], newlamb[0])