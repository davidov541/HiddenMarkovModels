'''
Created on Dec 18, 2009

@author: David McGinnis
'''

def PrintLambda(A, Pi):
    print "A:\n[",
    for i in range(0, len(A)):
        print "[",
        for j in range(0, len(A[0])):
            print A[i][j],
        print "]"
    print "]"
    print "Pi:\n[",
    for i in range(0, len(Pi)):
        print Pi[i],
    print "]"
    
def PrintLambda2(A, B, Pi):
    print "A:\n[",
    for i in range(0, len(A)):
        print "[",
        for j in range(0, len(A[0])):
            print A[i][j],
        print "]"
    print "]"
    print "B:\n[",
    for i in range(0, len(B)):
        print "[",
        for j in range(0, len(B[0])):
            print B[i][j],
        print "]"
    print "]"
    print "Pi:\n[",
    for i in range(0, len(Pi)):
        print Pi[i],
    print "]"
    
def PrintOutputs(Outputs):
    print "Outputs:"
    for output in Outputs:
        for state in output:
            print state,
        print "\n",
        
def PrintStateAndOutputs(Q, O):
    for i in range(0, len(Q)):
        print "Rep " + str(i + 1)
        print "States: ",
        for state in Q[i]:
            print str(state) + "\t",
        print "\nOutput: ",
        for output in O[i]:
            print str(output) + "\t",
        print "\n\n",