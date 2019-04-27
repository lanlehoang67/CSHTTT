import numpy as np



def modify(R):
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j] != 0:
                R[j][i] = 1/R[i][j]
    for i in range(len(R)):
        for j in range(len(R)):
            for k in range(len(R)):
                if R[i][j] != 0 and R[j][k] != 0:
                    R[i][k] = R[i][j] * R[j][k]
    return R
def modify2(R):
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j] != 0:
                R[j][i] = 1/R[i][j]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j-1] != 0 and R[j-1][j] !=0:
                R[i][j] = R[i][j-1] * R[j-1][j]
    for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j] != 0:
                R[j][i] = 1/R[i][j]
    return R
R =  np.array([
    [1,   1/5,  3,   4],
    [0, 1,  0,   0],
    [0,   0,  1,   0],
    [0,   0,  0, 1]
])
print(modify2(R))