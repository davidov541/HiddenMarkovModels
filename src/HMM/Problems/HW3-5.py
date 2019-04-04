'''
Created on Dec 17, 2009

@author: David McGinnis
'''

from Util.LL_MM import LL_MM
from math import log

"""
Hertz and Avis car rental agencies each have three locations which rent cars.
The output represents the location of a certain car each night.
Given the output and markov models below (1 is Avis, 2 is Hertz), which agency
is the car likely to be from?
"""
if __name__ == '__main__':
    Pi1 = [0.6, 0.2, 0.2]
    Pi2 = [0.3, 0.3, 0.4]
    A1 = [[0.8, 0.1, 0.1], [0.3, 0.2, 0.5], [0.2, 0.6, 0.2]]
    A2 = [[0.2, 0.7, 0.1], [0.3, 0.3, 0.4], [0.2, 0.2, 0.6]]
    Q = [0, 1, 2, 2, 2, 2, 2, 0, 1, 0]
    Score1 = LL_MM(Pi1, A1, Q)
    Score2 = LL_MM(Pi2, A2, Q)
    print log(Score1 / Score2, 10)