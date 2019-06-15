# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:41:57 2019

@author: Stella
"""


def betteroff(port_q):
    for i in range(4):
        x = -1/math.log(port_q[i].loc[:, "Q"].mean())
        r = -1/math.log(port_q[i].loc[port_q[i]["Ranking"]==1, "Q"].values[0])
        print(i, (x-r)/x)
    