# Copyright (c) 2014 Chen Zhaoqiang DDDC SIMM
#qq 744891290 qqgroup 144539789
# A PyMOL script for drawing a CGO box by the coordinate of the center,and the size of box
#center_x,center_y,center_z,size_x,size_y,size_z,


import pymol
from pymol import cmd
from pymol.wizard import Wizard
from chempy import cpv
from pymol.cgo import *
from pprint import pprint

def gridboxbyatomid2tetra(atomid1,atomid2,atomid3,atomid4,obj="all",name="tetrabox",r1=1,g1=0,b1=1,trasp=0):
    """
    DESCRIPTION
    Create a box from the center coordinate of the box and the size of box
    
    USAGE
    run gridbox.py
    1the simplest
    gridbox center_x,center_y,center_z,size_x,size_y,size_z
    2rename the box object
    gridbox center_x,center_y,center_z,size_x,size_y,size_z,name,
    3set the color of the box object
    gridbox center_x,center_y,center_z,size_x,size_y,size_z,name,r1,g1,b1
    4set the trasp of the box
    gridbox center_x,center_y,center_z,size_x,size_y,size_z,name,r1,g1,b1,trasp
    
    ps:the value of r1,g1,b1 trasp   range  is 0-1
       trasp=1,no trasprent
    
    
    """
    r1=float(r1)
    g1=float(g1)
    b1=float(b1)
    trasp=float(trasp)
    
    com = obj + " and id "+atomid1
    print com
    
    atom1xyz = cmd.get_model( com   ).atom[0].coord

    pprint(atom1xyz)

    com = obj + " and id "+atomid1   
    p1 = cmd.get_model( com   ).atom[0].coord

    com = obj + " and id "+atomid2
    p2 = cmd.get_model( com   ).atom[0].coord

    com = obj + " and id "+atomid3
    p3 = cmd.get_model( com   ).atom[0].coord

    com = obj + " and id "+atomid4
    p4 = cmd.get_model( com   ).atom[0].coord




    obj1=[
            #  ALPHA,trasp,
            #  COLOR,r1,g1,b1,
             BEGIN, TRIANGLES,
             VERTEX,p1[0],p1[1],p1[2],
             VERTEX,p2[0],p2[1],p2[2],

             VERTEX,p3[0],p3[1],p3[2],
             END,
           ]
    obj2 = [
            #  ALPHA,trasp,
             BEGIN, TRIANGLES,
			#  COLOR,1,0,0,

             VERTEX,p1[0],p1[1],p1[2],
             VERTEX,p2[0],p2[1],p2[2],
             VERTEX,p4[0],p4[1],p4[2],

             END,
            ] 
    obj3 = [     
            #  ALPHA,trasp,    
             BEGIN, TRIANGLES,
            #  COLOR,1,0,0,
             VERTEX,p2[0],p2[1],p2[2],
             VERTEX,p4[0],p4[1],p4[2],
             VERTEX,p3[0],p3[1],p3[2],
             END,
    ]

    obj4 = [
             
             BEGIN, TRIANGLES,
            #  COLOR,1,0,0,
             VERTEX,p1[0],p1[1],p1[2],

             VERTEX,p4[0],p4[1],p4[2],
             VERTEX,p3[0],p3[1],p3[2],
             END,
    ] 


             
    cmd.load_cgo(obj1, name+"1")
    cmd.load_cgo(obj2, name+"2")
    cmd.load_cgo(obj3, name+"3")
    cmd.load_cgo(obj4, name+"4")
    # cmd.create_o
    


cmd.extend('gridboxbyatomid2tetra', gridboxbyatomid2tetra)