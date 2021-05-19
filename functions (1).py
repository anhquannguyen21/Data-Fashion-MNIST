"""
Sample code automatically generated on 2020-07-08 03:48:18

by www.matrixcalculus.org

from input

d/dA A+B = eye\otimes eye

where

A is a matrix
B is a matrix

The generated code is provided "as is" without warranty of any kind.
"""

from __future__ import division, print_function, absolute_import

import numpy as np

def fAndG(A, B):
    assert isinstance(A, np.ndarray)
    dim = A.shape
    assert len(dim) == 2
    A_rows = dim[0]
    A_cols = dim[1]
    assert isinstance(B, np.ndarray)
    dim = B.shape
    assert len(dim) == 2
    B_rows = dim[0]
    B_cols = dim[1]
    assert A_rows == B_rows
    assert B_cols == A_cols

    functionValue = (A + B)
    gradient = np.einsum('ik, jl', np.eye(A_rows, A_rows), np.eye(B_cols, A_cols))

    return functionValue, gradient

def checkGradient(A, B):
    # numerical gradient checking
    # f(x + t * delta) - f(x - t * delta) / (2t)
    # should be roughly equal to inner product <g, delta>
    t = 1E-6
    delta = np.random.randn(3, 3)
    f1, _ = fAndG(A + t * delta, B)
    f2, _ = fAndG(A - t * delta, B)
    f, g = fAndG(A, B)
    print('approximation error',
          np.linalg.norm((f1 - f2) / (2*t) - np.tensordot(g, delta, axes=2)))

def generateRandomData():
    A = np.random.randn(3, 3)
    B = np.random.randn(3, 3)

    return A, B

if __name__ == '__main__':
    A, B = generateRandomData()
    functionValue, gradient = fAndG(A, B)
    print('functionValue = ', functionValue)
    print('gradient = ', gradient)

    print('numerical gradient checking ...')
    checkGradient(A, B)
