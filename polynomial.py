import matplotlib.pyplot as plt
import numpy as np

def betas_fit(x,betas):
    y_pred = list()
    for x_val in x:
        y_val = 0
        for deg in range(0,degree+1):
            if deg == 0:
                y_val += float(betas[deg])
            else:
                y_val += float(betas[deg]) * (x_val**deg)
        y_pred.append(y_val)   

    return y_pred



def poly_fit(x,y,degree):

    vals = list()
    for deg in range(0,degree+1):
        deg_list = list()
        for v in x:
            deg_list.append(v**deg)
        vals.append(deg_list)
    X = np.matrix(vals).transpose()
    Y = np.matrix(y).transpose()
    

    betas = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
    y_pred = betas_fit(x,betas)

    return y_pred, betas


    
    