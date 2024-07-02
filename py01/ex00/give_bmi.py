import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    
    """
    height_array = np.array(height)
    weight_array = np.array(weight)
    bmi_values = weight_array / (height_array ** 2)
    return bmi_values.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi_array =  np.array(bmi)
    result = bmi_array > limit
    return result.tolist()

"""
ref:
https://www.geeksforgeeks.org/vectorized-operations-in-numpy/
https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/VectorizedOperations.html
"""