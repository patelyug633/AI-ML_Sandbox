import numpy as np
class Losses:

    def Branin(X,Y):
       # Branin function with standard constants
        a = 1
        b = 5.1 / (4 * np.pi**2)
        c = 5 / np.pi
        r = 6
        s = 10
        t = 1 / (8 * np.pi)

        Z = a * (Y - b * X**2 + c * X - r)**2 + s * (1 - t) * np.cos(X) + s
        return Z 
    
    def Branin_der(X,Y):
        a = 1
        b = 5.1 / (4 * np.pi**2)
        c = 5 / np.pi
        r = 6
        s = 10
        t = 1 / (8 * np.pi)
        def Branin_derx():
            return 2*(Y - b * X**2 + c * X - r)*(b*X + c)  - s*(1-t)*np.sin(X)
        def Branin_derY():
            return 2*(Y - b * X**2 + c * X - r)
        return Branin_derx(), Branin_derY()
    def Branin_coor():
        x = (-5, 10, 100)
        y = (0, 15, 100)
        return x, y
    
    def contour_coor():
        x = (0,8,100)
        y = (1,8,100)
        return x, y

    def Paraboloid(X,Y):
        return X**2 + Y**2
    
    def contour(X,Y):
        return np.sin(X) + np.cos(Y)