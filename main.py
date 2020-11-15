import sys
import package.readtxt as readtxt
#Checking if the matrix file is given
if len(sys.argv)==1:
    print("Matrix file is not passed")
    
else:
    if sys.argv[1]=="m1.txt" or sys.argv[1]=="m2.txt" or sys.argv[1]=="m3.txt" or sys.argv[1]=="m4.txt":
        readtxt.readMatrix(sys.argv[1])

    else:
        print("Matrix file is not passed")
        
