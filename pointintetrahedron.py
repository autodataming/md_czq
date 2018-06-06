#!python2

import numpy as np 
from numpy.linalg import det 
from pprint import  pprint 
from point_in_triangle import point_in_triangle

def pointintetrahedron(V1,V2,V3,V4,P1):
    '''
    

    ''' 
    V1.append(1)
    V2.append(1)
    V3.append(1)
    V4.append(1) 
    P1.append(1)
    # pprint([V1,V2,V3,V4])
    D0 = det(np.array( [V1,V2,V3,V4]))
    # # D0 = det(a)
    # print "D0",D0
    # D1
    D1 = det(np.array( [P1,V2,V3,V4]))
    # D2
    D2 = det(np.array( [V1,P1,V3,V4]))
    # pprint([V1,P1,V3,V4])
    # D3
    D3 = det(np.array( [V1,V2,P1,V4]))
    # D4
    D4 = det(np.array( [V1,V2,V3,P1]))
    # print "D1 D2 D3 D4"
    pprint([V1,V2,V3,V4,P1])
    print D0,D1,D2,D3,D4

    # for D in [D0,D1,D2,D3,D4]:
    #     if D < 0.00001 and D > -0.0001:
    #         print "!!!!! the tetrahedron may coplan OR the point i in boudries 3 point (except i)"
    


    if D0 > 0 and D1>0 and D2>0 and D3>0 and D4>0:
        # print "the point in the tertrahedron"
        flag = 1
    elif D0 < 0 and D1<0 and D2<0 and D3<0 and D4<0:
        # print "the point in the tertrahedron"
        flag = 1
    elif D1 == 0:
        flag = point_in_triangle(V2,V3,V4,P1)
    elif D2 == 0:
        flag = point_in_triangle(V1,V3,V4,P1)
    elif D3 == 0:
        flag = point_in_triangle(V2,V1,V4,P1)
    elif D4 == 0:
        flag = point_in_triangle(V2,V3,V1,P1)
        # print "the point not in the tertrahedron"
    else:
        flag = 0
    return flag





if __name__ == '__main__':
    V1=[0,0,0]
    V2=[0,10,0]
    V3=[10,10,0]
    V4=[0,10,10]

    P1=[2,10,2]
    P2=[5,5,5]
    flag = pointintetrahedron(V1,V2,V3,V4,P1)
    print flag
    V1=[0,0,0]
    V2=[0,10,0]
    V3=[10,10,0]
    V4=[5,5,5]
    P1=[5,5,1]
    P2=[4,4,4]
    flag = pointintetrahedron(V1,V2,V3,V4,P2)
    print flag
