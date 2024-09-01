"""
Code implementing fake news algorithm for incomplete markets model,
as built in econ411_3_lecture7.ipynb.

Computes sequence-space Jacobians for any list of shocked
inputs to the household problem (any given input shock can be some
combination of shock to 'y', 'r', 'beta', and 'eis'), always returns
Jacobians for outputs 'A' and 'C'.
"""

import numpy as np
import sim_steady_state_fast as sim


def jacobian(ss, shocks, T):
    """Gives Jacobian of A and C at horizon 'T' of standard incomplete markets
    model around steady state 'ss', with respect to each input shock in 'shocks'.
    'shocks' is a dict with entries (i, shock), where i is the arbitrary
    name given to a shock, and 'shock' is itself a dict with entries
    (k, dx) that specify by how much 'dx' shock perturbs each input 'k'."""

    # step 1 for all shocks i, allocate to curlyY[o][i] and curlyD[i]
    curlyY = {'A': {}, 'C': {}}
    curlyD = {}
    for i, shock in shocks.items():
        curlyYi, curlyD[i] = step1_backward(ss, shock, T, 1E-4)
        curlyY['A'][i], curlyY['C'][i] = curlyYi['A'], curlyYi['C']
    
    # step 2 for all outputs o of interest (here A and C)
    curlyE = {}
    for o in ('A', 'C'):
        curlyE[o] = sim.expectation_functions(ss[o.lower()], ss['Pi'], ss['a_i'], ss['a_pi'], T-1)
                                            
    # steps 3 and 4: build fake news matrices, convert to Jacobians
    Js = {'A': {}, 'C': {}}
    for o in Js:
        for i in shocks:
            F = np.empty((T, T))
            F[0, :] = curlyY[o][i]
            F[1:, :] = curlyE[o].reshape(T-1, -1) @ curlyD[i].reshape(T, -1).T
            Js[o][i] = J_from_F(F)
    
    return Js


def step1_backward(ss, shock, T, h=1E-4):
    """Performs step 1 of fake news algorithm, finding curlyY and curlyD up to
    horizon T given 'shock', which is a dict mapping inputs 'k' to how much they
    are shocked by. Use one-sided numerical diff, scaling down shock by 'h'."""

    # preliminaries: obtain D_1 with no shock, ss inputs to backward_iteration
    D1_noshock = sim.forward_iteration(ss['D'], ss['Pi'], ss['a_i'], ss['a_pi'])
    ss_inputs = {k: ss[k] for k in ('Va', 'Pi', 'a_grid', 'y', 'r', 'beta', 'eis')}
    
    # allocate space for results
    curlyY = {'A': np.empty(T), 'C': np.empty(T)}
    curlyD = np.empty((T,) + ss['D'].shape)
    
    # backward iterate
    for s in range(T):
        if s == 0:
            # at horizon of s=0, 'shock' actually hits, override ss_inputs with shock
            shocked_inputs = {k: ss[k] + h*shock[k] for k in shock}
            Va, a, c = sim.backward_iteration(**{**ss_inputs, **shocked_inputs})
        else:
            # now the only effect is anticipation, so it's just Va being different
            Va, a, c = sim.backward_iteration(**{**ss_inputs, 'Va': Va})
        
        # aggregate effects on A and C
        curlyY['A'][s] = np.vdot(ss['D'], a - ss['a']) / h
        curlyY['C'][s] = np.vdot(ss['D'], c - ss['c']) / h
        
        # what is effect on one-period-ahead distribution?
        a_i_shocked, a_pi_shocked = sim.interpolate_lottery_loop(a, ss['a_grid'])
        curlyD[s] = (sim.forward_iteration(ss['D'], ss['Pi'], a_i_shocked, a_pi_shocked) - D1_noshock) / h
        
    return curlyY, curlyD


def J_from_F(F):
    """Recursion J(t,s) = J(t-1,s-1) + F(t,s) to build Jacobian J from fake news F"""
    J = F.copy()
    for t in range(1, F.shape[0]):
        J[1:, t] += J[:-1, t-1]
    return J
