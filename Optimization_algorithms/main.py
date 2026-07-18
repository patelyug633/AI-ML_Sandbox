import numpy as np
from visualizer import Visualizer as vis
from loss_func import Losses as Loss

def funcZ(X,Y):
   # Branin function with standard constants
    a = 1
    b = 5.1 / (4 * np.pi**2)
    c = 5 / np.pi
    r = 6
    s = 10
    t = 1 / (8 * np.pi)
    
    Z = a * (Y - b * X**2 + c * X - r)**2 + s * (1 - t) * np.cos(X) + s
    return Z 

# Domain for Branin function
bx, by = Loss.Branin_coor()
x, y = Loss.contour_coor()
screen = vis(bx, by, Loss.Branin)
screen.show_graph()
