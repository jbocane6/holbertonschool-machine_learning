#!/usr/bin/env python3
import numpy as np
"""Calculates the shape of a matrix"""

def matrix_shape(matrix):
    """
    matrix_shape: validates that array is not null and get the shape
    
    Returns: The shape should be returned as a list of integers
    """
    if type(matrix) is list:
        return [len(matrix), *matrix_shape(matrix[0])]
    else:
        return []
 