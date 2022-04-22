from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get("")
def get_matrix() -> dict:
    matrix_a = np.random.randint(100, size=[10, 10])
    matrix_b = np.random.randint(100, size=[10, 10])
    product = matrix_a * matrix_b
    matrix_a = np.array2string(matrix_a)
    matrix_b = np.array2string(matrix_b)
    product = np.array2string(product)
    return {'msg': { 'matrix_a': matrix_a, 'matrix_b': matrix_b, 'product': product }}