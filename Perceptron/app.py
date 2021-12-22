from Perceptron import Perceptron

inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
outputs = [0, 0, 0, 1]

percep = Perceptron(4, 5, 0.75)

percep.train(inputs, outputs)

percep.predict(inputs)
