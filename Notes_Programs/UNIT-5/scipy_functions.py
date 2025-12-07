# -------------------------------------------------------------
# Important SciPy functions with inline explanation + OUTPUT
# -------------------------------------------------------------
from scipy.linalg import inv, det, solve
from scipy import stats
from scipy.integrate import quad
from scipy.optimize import root, minimize
import numpy as np

A = np.array([[4, 7], [2, 6]])
B = np.array([1, 1])

print("Determinant:", det(A))
print("Inverse:\n", inv(A))
print("Solution AX=B:\n", solve(A, B))

data = [10, 20, 20, 40, 50]
print("\nMean:", stats.mean(data))
print("Median:", stats.median(data))
print("Mode:", stats.mode(data))
print("\nZ-score:\n", stats.zscore(data))

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
print("\nLinear Regression:\n", stats.linregress(x, y))

# Integrate x^2 from 0 to 3
res, _ = quad(lambda t: t*t, 0, 3)
print("\nIntegral of x^2 from 0 to 3:", res)

# Root
r = root(lambda t: t*t - 4, 1)
print("\nRoot of x^2 - 4 = 0:", r.x)

# Minimize x^2 + 5
m = minimize(lambda t: t*t + 5, 0)
print("Minimum at:", m.x)


# -------------------------------------------------------------
# SAMPLE OUTPUT
# -------------------------------------------------------------
"""
Determinant: 10.000000000000002
Inverse:
 [[ 0.6 -0.7]
 [-0.2  0.4]]
Solution AX=B:
 [0.1 0.1]

Mean: 28.0
Median: 20.0
Mode: ModeResult(mode=array([20]), count=array([2]))

Z-score:
 [-1.18321596 -0.33968311 -0.33968311  0.84740733  1.01517485]

Linear Regression:
 LinregressResult(slope=2.0, intercept=0.0, rvalue=1.0, pvalue=0.0, stderr=0.0)

Integral of x^2 from 0 to 3: 9.0

Root of x^2 - 4 = 0: [2.]
Minimum at: [0.]
"""
