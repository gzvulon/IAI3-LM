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
import s_learning_curve_common_verbs
import scp

N=10

simpleClass = s_learning_curve_simple. MakeAgentLimitedClass(N)
blackClass  = s_learning_curve_black_list.MakeAgentClass(N)
steemClass =  s_learning_curve_sttemming.MakeAgentClass(N)
bothClass = s_learning_curve_both_back_stemming.MakeAgentClass(N)
ourClass   = s_learning_curve_common_verbs.MakeAgentClass(N)

agentClassPairs = [ 
    (ourClass,bothClass)
    (ourClass,simpleClass)
    ]


params = {
    scp.X_POINTS : 20, #not relevat
    scp.STEP :     5, #not relevat
    scp.NUM_FOLDS : 10,
    scp.CLASSIFY_TIME : 2,
    scp.LEARN_TIME : 60*2,
    scp.SEED : 1
}

s_bech_vs.main(agentClassPairs,params)