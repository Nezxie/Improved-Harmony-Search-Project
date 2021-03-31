import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')
import numpy as np

def PlotContour(X, Y, Z, PointsTuple, RigidContours=False, 
                GraphLayers=30, GraphColour='coolwarm', 
                PointsSize=10, PointsColour='black'):

    if RigidContours:
        plt.contour(X, Y, Z, colors='black', linewidths=0.3)

    plt.contourf(X, Y, Z, GraphLayers, cmap=GraphColour)
    plt.colorbar()

    plt.scatter(*zip(PointsTuple), s=PointsSize, c=PointsColour)

    plt.show()
    

if __name__ == '__main__':
    def f(x, y):
        return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
        # return (x-2.5)**2 + (y-2.5)**2

    x = np.linspace(0, 5, 50)
    y = np.linspace(0, 5, 50)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    N = 8
    xx = 5*np.random.rand(N)
    yy = 5*np.random.rand(N)
    xylist = (xx, yy)

    PlotContour(X, Y, Z, xylist, True, 10) #, PointsSize=5, PointsColour='white')
