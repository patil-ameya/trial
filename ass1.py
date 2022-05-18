import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
from regex import B

style.use('ggplot')
x_cords=np.array([10,9,2,15,10,16,11,16],dtype=np.float64)
y_cords=np.array([95,80,10,50,45,98,38,93],dtype=np.float64)

def best_fit_slope(x_cords,y_cords):
    x_mean=np.sum(x_cords)/np.size(x_cords)
    y_mean=np.sum(y_cords)/np.size(y_cords)
    xy_mean=(np.sum(x_cords*y_cords)/np.size(x_cords))
    x_mean_sq=x_mean*x_mean
    x_sq_mean=(np.sum(x_cords*x_cords)/np.size(x_cords))
    b1=(((x_mean*y_mean)-xy_mean)/(x_mean_sq-x_sq_mean))
    b0=(y_mean-(b1*x_mean))
    return b1,b0

b1,b0=best_fit_slope(x_cords,y_cords)
regression_line=[(b1*x)+b0 for x in x_cords]
predict_x=20
predict_y=(b1*predict_x)+b0
plt.scatter(x_cords,y_cords,color='b',label='data_points')
plt.scatter(predict_x,predict_y,color='g')
plt.plot(x_cords,regression_line,label='line')
plt.legend(loc=4)
plt.show()

print("y=",b1,'x+',b0)
