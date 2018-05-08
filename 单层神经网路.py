import numpy as np
import matplotlib.pyplot as plt
X = np.array([[1, 3, 3], [1, 4, 3], [1, 1, 1]])
W = (np.random.rand(3) - 0.5) * 2
print(W)
Y = np.array([1, 1, -1])
print(Y)
print (Y.T)
Ir = 0.11
num = 0
o = 0
def update():
    global X, Y, W, Ir, num
    num+=1
    o = np.sign(np.dot(X, W.T))
    W_C =  Ir * (np.dot((Y - o.T), X))
    W =  W  + W_C
for _ in range(100):
    update()
    print(W)
    print(num)
    o =np.sign(np.dot(X, W.T))
    print (o)
    
    if (o == Y.T).all():
        print("Finished")
        print(num)
        break;
x1 = [3, 4]
y1 = [3, 3]
x2 = [1]
y2 = [1]
k = -W[1] / W[2]
b = -W[0] / W[2]
xdata = np.linspace(0, 5)
plt.figure()
plt.plot(xdata, xdata*k+b, 'r')
plt.plot(x1, y1, 'bo')
plt.plot(x2, y2, 'yo')
plt.show()