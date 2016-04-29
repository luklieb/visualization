#Copyright 2016 FAU Erlangen-Nürnberg for educational purposes only


from math import fabs

def linearInterpolate(points, value):
	#perform linear interpolation based on the point's elevation value
	#return the interpolated point as tuple (x, y, z)
	
def extractLineSegment(points, value):
	#Take the three points of a cell and extract the iso line segments use the function linearInterpolate
	#for linear interpolation along the edges
		

#retrieve ParaView polydata objects
pdi = self.GetPolyDataInput()
pdo = self.GetPolyDataOutput()

#define vtkPoints object for writing points to
pts = 

#retrieve the elevation data that was added by the elevation filter
pointElevation = 

#get all cells of pdi


#loop over all 25 isolines
for j in ...
	#loop over all cells in pdi and generate points
	for i in ...
	 	#get information about cell (points the cell consists of, elevation information per point, ...)
		
		#pack all information that is needed to extract a line segment into one data structure of the form
		#triPoints = ((point1 X, point1 Y, point1 Z), point1 Elevation), ...)
		triPoints = 
		
		#call function extractLineSegment using triPoints and retrieve points of line segment
		linePoints = 
		
		#add points to output (vtkPoints object)

#add points to pdo

#allocate appropriate number of cells (lines) in pdo

#loop over points, create cells (lines) every two consecutive points form a line segment
for i in ...
