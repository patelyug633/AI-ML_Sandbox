from loss_func import Losses
class Optimizers:
    def __init__(self):
        self.lR  = 0.01
        self.delta = 0.9
        self.momentum = None
    
    def SGD(self,X,Y):
        gX, gY = Losses.Branin_der(X,Y)

        X = X - 0.1 *gX
        Y = Y - 0.1 *gY

        return X, Y
    
    def SGDM(self, X, Y):
        if self.momentum == None:
            gx, gy = Losses.Branin_der(X,Y)
            self.momentum = self.lR * gx , self.lR * gy
        else:
            gx, gy = Losses.Branin_der(X,Y)
            mgx, mgy = self.momentum
            self.momentum = self.delta*mgx + self.lR*gx, self.delta*mgy + self.lR*gy
        
        gx, gy = self.momentum
        X = X - gx
        Y = X - gy

        return X, Y



