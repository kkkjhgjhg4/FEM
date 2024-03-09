#!/usr/bin/env python3

import numpy as np
import FEData as model

def solve_penalty():
    nd = model.nd; neq=model.neq
    K = model.K
    f = model.f
    d = model.d
    
    beta = np.mean(np.trace(K)) * 1e7
    
    for i in range(nd):
        K[i, i] = beta
        f[i] = beta * model.d[i]

    # solve for d
    d= np.linalg.solve(K, f) 
    model.d = d

    # compute the reaction r
    f = - beta * model.d[0:nd] # f[20] is external force

    # write to the workspace
    print('\nsolution d');  print(model.d)
    print('\nreaction f =', f)

    return f