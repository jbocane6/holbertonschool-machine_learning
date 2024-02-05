#!/usr/bin/env python3
import numpy as np

def matrix_shape(matrix):
    """
    matrix_shape: validates that array is not null and get se shape
    """
    if not matrix:
        return
    arr = np.array(matrix)
    return arr.shape
