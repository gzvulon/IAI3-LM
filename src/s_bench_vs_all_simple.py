# -*- coding:utf-8 -*-
"""
Created on Jun 24, 2011

@author: inesmeya
"""

import s_learning_curve_simple
import s_learning_curve_black_list
import s_learning_curve_sttemming
import s_learning_curve_both_back_stemming
import s_bech_vs

N=10

simpleClass = s_learning_curve_simple. MakeAgentLimitedClass(N)
blackClass  = s_learning_curve_black_list.MakeAgentClass(N)
steemClass =  s_learning_curve_sttemming.MakeAgentClass(N)
bothClass = s_learning_curve_both_back_stemming.MakeAgentClass(N)

agentClassPairs = [ 
    (steemClass, simpleClass),
    (blackClass, simpleClass),
    (bothClass, simpleClass)
    ]

s_bech_vs.main(agentClassPairs)