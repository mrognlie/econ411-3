import numpy as np

def compute_lifecycle(r, sigma, beta, y, Phi):
    J = len(beta)
    q = (1+r)**(-np.arange(J))                   # present-value discounting q_j = (1+r)^(-j)
    theta = (1+r)**(sigma*np.arange(J)) * (beta / beta[0])**sigma
    c0 = (q @ (Phi * y)) / (q @ (Phi * theta))
    c = theta * c0

    phi = np.append(Phi[1:], 0) / Phi            # phi_j = Phi_{j+1} / Phi_j

    # iterate backward to get assets at each age (could accelerate using Numba in richer case)
    a = np.zeros(J)
    a[J-1] = (c[J-1] - y[J-1])/(1+r)
    for j in range(J-2, -1, -1):
        a[j] = (c[j] - y[j] + phi[j]*a[j+1])/(1+r)
    
    return c, a


def gompertz_survival(t, b, c):
    return np.exp(-b/c * (np.exp(c * t) - 1))

