
inputs = [[0,0],[0,1],[1,0],[1,1]]
outputs = [0,0,0,1]

erreur = []

comp = []

for w1 in range(-5,6):
    for w2 in range(-5,6):
        for i in inputs:
            sol=w1*i[0]+w2*i[1]
            e = 0.5*(sol-outputs[i])
            comp.append(sol,e)
