# -*- coding: utf-8 -*-
# Applied Visualization
# Class to handle 3D vector fields defined on uniform grids.

## @package VectorField
## @brief Impelements a 3D vector field on an uniform grid and corresponding trilinear interpolation.

import struct
import array
import math


## This class implements a vector field defined on a uniform grid inclusive trilinear
## interpolation.
#
# This is a container class including methods for reading the 
# vector field data from a binary file, accessing vector components
# per node and interpolating the vector field at a position in space using
# trilinear interpolation. The data is stored in a 1D array in linear order.
# Therefore, to access data a the node (i,j,k) in the 3D uniform grid,
# the index must be mapped to
# \f[
#     index = 3\times(i + j\times xdim + k \times xdim \times ydim)
# \f]
# where the index corresponding the the x-coordinate is the fastest, then the
# index corresponding to the y-coordinate and finally the index conrrespoing
# to the z-coordinate.
#
#  <b>Exported class: </b> <c>VectorField</c>
#
#  @author Roberto Grosso
#  @date March 2012
#  @copyright Universität Erlangen-Nürnberg

class VectorField:
    ## Default constructor.    
    #
    # @param self reference to the object instance.
    def __init__(self):
        self.data  = array.array('d')
        self.xdim  = 0
        self.ydim  = 0
        self.zdim  = 0
        self.dx    = 0.0
        self.dy    = 0.0
        self.dz    = 0.0
        self.xMin  = 0.0
        self.xMax  = 0.0
        self.yMin  = 0.0
        self.yMax  = 0.0
        self.zMin  = 0.0
        self.zMax  = 0.0

    ## Read a uniform vector field from a binary file.
    #  The data must be stored in the following format:
    #  @li 3 ints containing the dimensions in x,y, and z.
    #  @li 3 doubles containing the spacing in x,y, an z.
    #  @li 6 doubles containing the bounding box, i.e. min/max for x,y, and z.
    #  @li a one dimensional array with the components of the velocity for each node.
    # 
    # @param self reference to the object instance.
    # @param filename a string containing the name of the file
    def read(self,filename):
        # open file and read sizes and domain information
        fl = open(filename,'rb')
        dims = struct.unpack('iii',fl.read(struct.calcsize('i')*3))
        domain = struct.unpack('ddddddddd',fl.read(struct.calcsize('d')*9))
        self.data.fromfile(fl,3*dims[0]*dims[1]*dims[2])

        # set class variables
        self.xdim = dims[0]
        self.ydim = dims[1]
        self.zdim = dims[2]
        self.dx   = domain[0]
        self.dy   = domain[1]
        self.dz   = domain[2]
        self.xMin = domain[3]
        self.xMax = domain[4]
        self.yMin = domain[5]
        self.yMax = domain[6]
        self.zMin = domain[7]
        self.zMax = domain[8]

    ## Access to vector data node wise by index.
    #
    # @param self reference to the object instance.
    # @param index 
    # @return a tuple with the three components of the velocity.
    def getData(self,index):
        # computes index of first velocity component.
        idx = 3*index;
        return (self.data[idx],self.data[idx+1],self.data[idx+2])

    ## Get the dimension of the uniform grid in x,y and z.
    #
    # @param self reference to the object instance.
    # @return a tuple with the dimensions in x,y, and z.
    def getSize(self):
        return (self.xdim,self.ydim,self.zdim)

    ## Get cell spacing in x,y, and z.
    #
    # @param self reference to the object instance.
    # @return a tuple with the cell size in x,y, and z.
    def getSpacing(self):
        return (self.dx,self.dy,self.dz)

    ## Get bounding box of uniform grid.
    #
    # @param self reference to the object instance.
    # @return a tuple with the 6 values defining the bounding box of the uniform grid.
    def getBBox(self):
        return (self.xMin,self.xMax,self.yMin,self.yMax,self.zMin,self.zMax)

    ## Operator overloaded implementing the tri-linear interpolation on a uniform grid.
    #  
    # @param self reference to the object instance.
    # @param x x-coordinate of position in space.
    # @param y y-coordinate of position in space. 
    # @param z z-coordinate of position in space.    
    # @return a tuple with a true or false if interpolation succeded and the interpolated values of the velocity.
    def __call__(self,x,y,z):
        return (True, 0, 0, 0)
        # Implement your code here
        # check if (x,y,z) is in the domain, return False in the first componente otherwise


        # compute indices and make sure the a index is always >= 0


        # check boundary cases


        # interpolate
        # find indices of cell containing the point 


        # compute offsets


        # tri-linear interpolaton

        # done return (True, val1, val2, val3)
