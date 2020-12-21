import numpy as np

def testAssert(val1, val2, string, max_error = 1e-4):
    # relative error of the computed values compared to reference values provided by badams
    string += ' %.4e != %.4e'%(val1, val2)
    return (np.isclose([val1], [val2], rtol=max_error), string)
