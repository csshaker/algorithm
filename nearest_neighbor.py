import pandas as pd
import math as m
import matplotlib.pyplot as plt

data = pd.read_csv('data1.csv')
height = list(data['Height'])
weight = list(data['Weight'])
size = list(data['Size'])
volume = len(height)

def NearestNeighbor(h, w):
    distance = []
    
    for i in range(volume):
        d = m.sqrt(m.pow(height[i] - h, 2) + m.pow(weight[i] - w, 2))
        distance.append(d)
    
    sm = min(distance)
    
    for i in range(volume):
        if distance[i] == sm:
            print('\nYour T shirt size is: ', size[i])
            height.append(h)
            weight.append(w)
            size.append(size[i])
            
            break
    h1 = []
    h2 = []
    w1 = []
    w2 = []    
    
    for i in range(len(height)):
        if size[i] == 'L':
            h1.append(height[i])
            w1.append(weight[i])
        
    for i in range(len(height)):
        if size[i] == 'M':
            h2.append(height[i])
            w2.append(weight[i])
    
    plt.clf()
    plt.scatter(h1, w1, marker='+', label='Large')
    plt.scatter(h2, w2, marker='*', label='Medium')
    plt.legend(loc=2)
    plt.show()
        
n = int(input('Enter the number of input: '))

for i in range(n):
    input_height = int(input('Enter the height: '))
    input_weight = int(input('Enter the weight: '))

    NearestNeighbor(input_height, input_weight)
