#!/usr/bin/env python3
"""Calculates the shape of a matrix"""

def matrix_shape(matrix):
    """
    matrix_shape: validates that array is not null and get the shape

    Returns: The shape should be returned as a list of integers
    """
    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + matrix_shape(matrix[0])
