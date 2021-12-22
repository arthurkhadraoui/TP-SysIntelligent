import csv




class Perceptron:

    def __init__(self,nbinputs,epochs,lr):
        self.nbinputs = nbinputs
        self.epochs = epochs
        self.lr = lr
        self.w0 = 0
        self.w1 = 0
        self.w2 = 0

    def train(self,inputs,outputs):
        for ep in range(self.epochs):
            for inp in range(self.nbinputs):
                    predic = self.w0+self.w1*inputs[inp][0]+self.w2*inputs[inp][1]
                    if predic>0:
                        predic=1
                    else:
                        predic=0
                    self.w0 = self.w0 + self.lr*(outputs[inp]-predic)
                    self.w1 = self.w1 + self.lr * (outputs[inp] - predic)*inputs[inp][0]
                    self.w2 = self.w2 + self.lr * (outputs[inp] - predic) *inputs[inp][1]
            print('epoch ',ep,': w0=',self.w0,', w1= ',self.w1,', w2= ',self.w2, ' predic= ',predic)
        header =['w0','w1','w2']
        with open('weights.csv', 'w',newline='',) as f:
            writer= csv.writer(f)
            writer.writerow(header)
            writer.writerow([self.w0,self.w1,self.w2])

    def predict(self,inputs):
        for i in range(len(inputs)):
            predic = self.w0 + self.w1 *inputs[i][0] +inputs[i][1]
            if predic > 0:
                predic = 1
            else:
                predic = 0
            print(inputs[i][0],'&', inputs[i][1],' = ',predic)