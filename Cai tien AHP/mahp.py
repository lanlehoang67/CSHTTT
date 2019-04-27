from ahp import AHP
import numpy as np
class MAHP1(AHP):
    def __init__(self,R):
        self.R = self.modify(R)
    def modify(self,R):
        for i in range(len(R)):
            for j in range(len(R)):
                R[j][i] = 1/R[i][j]
                for k in range(len(R)):
                    R[i][k] = R[i][j] * R[j][k]
        return R
R =np.array( [
    [1,5,9],
    [1,1,3],
    [1,1,1]
])
RI= np.array([
    0,0,0.52,0.89,1.11,1.25,1.35,1.40,1.45,1.49,1.52,1.54,1.56,1.58,1.59
])
mahp = MAHP1(R)
print(mahp.R)