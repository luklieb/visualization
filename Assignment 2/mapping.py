#Copyright 2016 FAU Erlangen-Nuernberg for educational purposes only

import sys

##Function to adress a 2-dimensional matrix
##using a 1-dimensional index.
##Function should return the value (1 number!) of the
##2-dimensional matrix using the 1-dimensional index
##one whould use, if the matrix was linearized row wise
def addressMatrixWith1dIndex(matrix, index, nrow, ncol):
    spalte = index%ncol
    zeile = (index - spalte)/ncol
    return matrix[zeile][spalte]


#matrix=( (1,2,3), (4,5,6), (7,8,9), (10, 11, 12))
#print(addressMatrixWith1dIndex(matrix, 0, 4, 3))


##Takes a 2dimensional matrix (represented by a list of lists)
##as input, linearizes it row wise and returns the resulting
##1d list
def convert2dTo1d(matrix, nrow, ncol):
    array = []
    for i in range(0,nrow):
        array += matrix[i]
    return array


#print(convert2dTo1d(matrix, 4,3))

##Takes a 1dimensional list as input, that is the result of
##a row wise linearized matrix
##and returns the 2dimensional matrix as a list of lists 
def convert1dTo2d(array, nrow, ncol):
    array = list(array)
    matrix = []
    
    for i in range(0,nrow):
        matrix +=[],
        for j in range(0,ncol):
            matrix[i] += array[i*ncol+j],

    return matrix

#array = (1,2,3,4,5,6,7,8,9,10)
#print(convert1dTo2d(array, 3, 3))


##Takes a images stored in a 1dimensional data array
##and prints it in form of a 2dimensional matrix
##Use sys.stdout.write("To print") instead of 
##print "To print" to avoid unwanted whitespaces and
##newlines
def printImage(array, nrow, ncol):
    matrix = convert1dTo2d(array,nrow,ncol)
    
    for i in range(0,nrow):
        for j in range(0,ncol):
            sys.stdout.write(str(matrix[i][j]))
        sys.stdout.write("\n")



#printImage(array,3,3)















