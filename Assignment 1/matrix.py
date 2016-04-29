
#Copyright 2016 FAU Erlangen-Nürnberg for educational purposes only

# ===================================================================
# DO NOT CHANGE THESE FUNCTIONS
#
# Matrix multiplication
# Matrices are two-dimensional tuples
#
def multiply( m0, m1 ):
    try:
        # multiplication by scalar
        float(m1)
        return tuple([ tuple([ e*m1 for e in r ]) for r in m0 ])
    except :
        pass
        
        
    #convert vector to matrix
    convert = ()
    if not isinstance(m1[0],tuple):
        for i in range(0,len(m1)):
            convert += ((m1[i],),)
        m1 = convert
        if len(m1) == len(m0[0])-1:
            m1 +=((1,),)

    # multiply matrices m0 x m1
    result = ()
    for i in range(0,len(m0)):
        rTmp = ()
        for j in range(0,len(m1[0])):
            val = 0;
            for k in range(0,len(m1)):
                m0_ = m0[i][k]
                m1_ = m1[k][j]
                val += m0_*m1_
            rTmp += (val,)
        result += (rTmp,)
    
    # convert one-colmun matrices back to vector (flat tuple)
    if len(result[0]) == 1:
        convert = ()
        for i in range(0,len(result)):
            convert += (result[i][0],)
        result = convert
    return result





# A01.1 (a)
# ========
# return a square identity matrix of size dim+1
# example: input:  dim=2
#		   output: ( (1,0,0),
#					 (0,1,0),
#					 (0,0,1) )
def identityMat( dim ):
    result = ()
    for i in range(0, dim):
        bla = dim-i-1
        result = result + ( (0,)*i + (1,) + (0,)*bla, )
    return result


#print(identityMat(2))

# A01.1 (b)
# ========
# return a quadratic scaling matrix of size len(s)+1
# the values in the tuple 's'  represent the scale factors
# of the respective diagonal elements
# example: input:  s=(2, 4, 7)
#		   output: ( (2,0,0,0),
#					 (0,4,0,0),
#					 (0,0,7,0),
#					 (0,0,0,1) )
def scaleMat( s ):
    matrix = ()
    length = len(s)
    for i in range(0, length):
        bla = length-i
        matrix += ( (0,)*i + (s[i],) + (0,)*bla, )
    matrix += ( (0,)*length + (1,),)
    return matrix

b = (4,2,7)
#print(scaleMat(b))

# A01.1 (c)
# ========
# return a quadratic translation matrix 
# that, when applied to a point, moves it by 't'
# example: input:  t=(4, 2)
#		   output: ( (1,0,4),
#					 (0,1,2),
#					 (0,0,1) )
def translationMat( t ):
    matrix = ()
    length = len(t)
    matrix = identityMat(length+1)
    matrix = list(matrix)
    for i in range(0, length):
        matrix[i]=list(matrix[i])
        matrix[i][length] = t[i]
        matrix[i]=tuple(matrix[i])
    matrix = tuple(matrix)
    return matrix


#print( translationMat(b))


# A01.2
# ========
# this method must return a matrix that scales around an 
# anchor point 'point'. This can, for instance, be used to 
# scale objects relativ to their current center of gravity.
# This method can be implemented in 3 lines by using the
# 'translationMat()' and 'scaleMat()' methods which you implemented
# in the previous assignment. 
def scaleRelativeMat( point, s ):
    point2=()
    for i in range(0, len(point)):
        point2 += (-point[i],)
    matrix = multiply( translationMat(point), multiply(scaleMat(s), translationMat(point2)) )
    return matrix

p=(3,4,5)
s = (1,2,3)
#print (scaleRelativeMat(p, s))


# A01.3
# ========
# this method must return a matrix that that maps the
# rectangle 'rectFrom' to the rectangle 'rectTo'.
# An axis-aligned rectangle is a tuple '( (xMin,yMin), (xMax,yMax) )'.
# To Test this method, use it in 'transformations.py'
# to map 'rectangle' to the given target rectangle
def mapRectangleMat( rectFrom, rectTo ):
    mFrom = [rectFrom[0][0]+0.5*(rectFrom[1][0]-rectFrom[0][0]), rectFrom[0][1]+0.5*(rectFrom[1][1]-rectFrom[0][1]) ]
    mTo = [rectTo[0][0]+0.5*(rectTo[1][0]-rectTo[0][0]), rectTo[0][1]+0.5*(rectTo[1][1]-rectTo[0][1]) ]
    mVec = [ mTo[0]-mFrom[0], mTo[1]-mFrom[1]  ]
    mVec = tuple(mVec)
    scale= [ (float(rectTo[1][0]-rectTo[0][0]))/(float(rectFrom[1][0]-rectFrom[0][0])), (float(rectTo[1][1]-rectTo[0][1]))/(float(rectFrom[1][1]-rectFrom[0][1]))   ]
    scale = tuple(scale)
    print(scale)
    matrix = multiply(translationMat(mVec), scaleRelativeMat(mFrom, scale))
    return matrix





print(mapRectangleMat( ((-2.0,-2.0),(0.0,0.0)), ((2.0,4.0),(4.0,7.0))     ))





















