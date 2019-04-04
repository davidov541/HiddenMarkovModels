'''
Created on Jan 25, 2010

@author: mcginnda
'''

from Util import Sim_HMM
from Util import Train_HMM
from Util import PrintUtil

if __name__ == '__main__':
    T = 10
    rep = 10
    N = 2
    M = 7
    Pi = [0.5, 0.5]
    A = [[0.7, 0.3], [0.3, 0.7]]
    B = [[0.0, 1.0/6.0, 1.0/6.0, 1.0/6.0, 1.0/6.0, 1.0/6.0, 1.0/6.0], [0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5]]
    print "Original Lambda: "
    PrintUtil.PrintLambda2(A, B, Pi)
    QAndO = Sim_HMM.simulate_HMM(Pi, A, B, T, rep)
    print "Simulated States and Output: "
    PrintUtil.PrintStateAndOutputs(QAndO[0], QAndO[1])
    lamb = Train_HMM.train_HMM(N, M, QAndO[0], QAndO[1])
    print "Predicted Lambda: "
    PrintUtil.PrintLambda2(A, B, Pi)