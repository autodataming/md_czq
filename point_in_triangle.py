#!python2764

# https://stackoverflow.com/questions/12642256/python-find-area-of-polygon-from-xyz-coordinates

#determinant of matrix a
def det(a):
    return a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[0][2]*a[1][1]*a[2][0] - a[0][1]*a[1][0]*a[2][2] - a[0][0]*a[1][2]*a[2][1]

#unit normal vector of plane defined by points a, b, and c
def unit_normal(a, b, c):
    x = det([[1,a[1],a[2]],
             [1,b[1],b[2]],
             [1,c[1],c[2]]])
    y = det([[a[0],1,a[2]],
             [b[0],1,b[2]],
             [c[0],1,c[2]]])
    z = det([[a[0],a[1],1],
             [b[0],b[1],1],
             [c[0],c[1],1]])

    magnitude = (x**2 + y**2 + z**2)**.5
    if magnitude:
        '''

        '''    
        return (x/magnitude, y/magnitude, z/magnitude)
    else:
        return (0,0,0)
#dot product of vectors a and b
def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

#cross product of vectors a and b
def cross(a, b):
    x = a[1] * b[2] - a[2] * b[1]
    y = a[2] * b[0] - a[0] * b[2]
    z = a[0] * b[1] - a[1] * b[0]
    return (x, y, z)

#area of polygon poly
def area(poly):
    if len(poly) < 3: # not a plane - no area
        return 0

    total = [0, 0, 0]
    for i in range(len(poly)):
        vi1 = poly[i]
        if i is len(poly)-1:
            vi2 = poly[0]
        else:
            vi2 = poly[i+1]
        prod = cross(vi1, vi2)
        total[0] += prod[0]
        total[1] += prod[1]
        total[2] += prod[2]
  
    result = dot(total, unit_normal(poly[0], poly[1], poly[2]))
    return abs(result/2)


def point_in_triangle(V1,V2,V3,P1):
    '''

    '''
    areatotal =  area([V1,V2,V3])
    area1 = area([V3,V2,P1])
    area2 = area([V1,P1,V3])
    area3 = area([V1,V2,P1])
    if(areatotal ==  area1 +  area2 +  area3):
        return True
    else:
        return False

if __name__ == '__main__':
    '''
    '''
    V1=[0,0,0]
    V2=[0,10,0]
    V3=[10,10,0]


    P1=[1,8,0]
    flag = point_in_triangle(V1,V2,V3,P1) 
    print flag
    V1=[0,0,0]
    V2=[0,10,0]
    V3=[10,10,0]


    P1=[5,1,0]
    flag = point_in_triangle(V1,V2,V3,P1) 
    print flag

    P1=[0,11,0]
    flag = point_in_triangle(V1,V2,V3,P1) 
    print flag
    
