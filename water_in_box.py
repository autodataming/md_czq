#!python2 
'''
judge Oxygen in H2O stay in the box
'''

from pprint import pprint
#    pointintetrahedron
from pointintetrahedron import pointintetrahedron

def getwaterbypdb(filename):
    '''
    usage:
    '''
    waters =[]
    fh = open(filename)
    for line in fh:
        if 'OW' in line and 'SOL' in line:
#             ATOM      5  OW  SOL     0      37.080  39.840 129.580  1.00  0.00           O  
#             ATOM      6  HW1 SOL     0      98.230  63.850 143.160  1.00  0.00           H  
            id,x,y,z =map(lambda i: float(i.strip()), [line[6:11],line[30:38],line[38:46],line[46:54]])
            id=int(id)
            water=[id,x,y,z]
            waters.append(water)
    return waters

def getboxbypdb(filename,ids):
    '''
    usage:
    '''
    vertexs =[]
    fh = open(filename)

    for line in fh:
        if line.startswith("ATOM"):
            id=int(line[6:11].strip())
            if id in ids:  
                print line,             
                id,x,y,z =map(lambda i: float(i.strip()), [line[6:11],line[30:38],line[38:46],line[46:54]])
                id=int(id)
                ver=[id,x,y,z]
                vertexs.append(ver)
    
    vertexsnex=[]
    for id in ids:
        for v in vertexs:
            if v[0] == id:
                vertexsnex.append(v)
    return vertexsnex


def getcenbypdb(filename,id):
    '''
    '''
    # vertexs =[]
    fh = open(filename)

    for line in fh:
        if line.startswith("ATOM"):
            idd=int(line[6:11].strip())
            if id == idd :
                id,x,y,z =map(lambda i: float(i.strip()), [line[6:11],line[30:38],line[38:46],line[46:54]])
                id=int(id)
                center = [id,x,y,z]
                return center

if __name__ == '__main__':
    '''

    '''
    pdbfile='1_up2.pdb'
    #[[id,x,y,z], [id,x,y,z],]
    waters=getwaterbypdb(pdbfile)

#pointsid1=[11745,982,2543,457]
# pointsid2=[11973,10104,2750,739]
# innerpoint=4855
    
    # select boxvetex1,id 11745+9882+2543+457+11973+10104+2750+739
    #       0   1    2    3  4        5   6    7
    ids=[11745,9882,2543,457,11973,10104,2750,739 ]
    # ids=[11745,9882,2543,457,11973,10104,2750,1118 ]
    #[[id,x,y,z], [id,x,y,z],]
    box_vertex = getboxbypdb(pdbfile,ids)

    centerid=9995
    center = getcenbypdb(pdbfile,centerid)

    tetras=[ 
          [1,2,3], #down
            [1,3,4],

              [5,6,7],  #upper
              [5,7,8],

              [1,2,6], #left
              [1,6,5],

              [3,7,4], #right
             [7,4,8],

              [6,2,3], #forward
              [6,3,7],

              [5,1,4],  #back
              [5,4,8]  
             
    ]
    #
    total_water_box=0
    pprint(waters)
    for water in waters:
        for tetra in tetras:
            
            V1,V2,V3=map(lambda i: box_vertex[i-1][1:], tetra)  #   [0,0,0]
            V4 = center[1:]

            P1=water[1:]
            # pprint(V1)
            # pprint(P1)
            flagg = pointintetrahedron(V1,V2,V3,V4,P1)
            if flagg:
                total_water_box += 1
                # print "number water ",total_water_box  
                # pprint(water)
                break
        if flagg == 0:
            print "the water not in box"
            pprint(water)

    print "number of waters in box",total_water_box           
                

