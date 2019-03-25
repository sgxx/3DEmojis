from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time,matplotlib
from numpy import pi as pi
from math import radians as radians
from math import sqrt as sqrt
from math import cos as cos
from math import sin as sin
from math import tan as tan
from math import atan as atan
import math
from random import choice as choice
import random
from PIL import Image

if __name__ == '__main__':

    count=0

    filepath=r'C:\Users\esa72\PycharmProjects\sgx\Date\201902\CoordTransfer\visualization\image'

    a=6378137
    b=6356752.314

    u = np.linspace(0, 2*pi, 1128 * 1)
    v = np.linspace(-pi / 8, pi / 8, 94 * 1)

    x=a*np.outer(np.cos(u),np.cos(v))
    y=a*np.outer(np.sin(u),np.cos(v))
    z=b*np.outer(np.ones(np.size(u)),np.sin(v))

    bm=Image.open(r'C:\Users\esa72\PycharmProjects\sgx\Date\201902\CoordTransfer\visualization\projection\blog\result.png')
    bm=np.array(bm)

    colors=[]

    print(bm.shape)
    print(x.shape)

    for i in range(bm.shape[1]-1,-1,-1):
        item=[]
        for j in range(bm.shape[0]-1,-1,-1):
            color="#{}{}{}".format(str.zfill(str(hex(bm[j][i][0]))[2:],2),str.zfill(str(hex(bm[j][i][1]))[2:],2),str.zfill(str(hex(bm[j][i][2]))[2:],2))
            if len(color)!=7:
                print(color)
            item.append(color)

        colors.append(item)

    colors=np.array(colors)
    print(colors.shape)

    count=0

    u0=pi/3
    v0=pi/3

    x0=a*cos(u0)*sin(v0)
    y0=a*sin(u0)*sin(v0)
    z0=b*cos(v0)

    fig=plt.figure()
    ax=fig.gca(projection='3d')

    plt.axis('off')

    ax.plot_surface(x,y,z,facecolors=colors,rstride=2,cstride=2)

    ax.set_xlim(-4500000,4500000)
    ax.set_ylim(-4500000,4500000)
    ax.set_zlim(-4500000,4500000)

    plt.show()

    count+=1
    print('count',count)
    plt.savefig(r"C:\Users\esa72\PycharmProjects\sgx\Date\201902\CoordTransfer\visualization\projection\image\{}.png".format(count))




