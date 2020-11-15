import package.displaydat as disdat

def readMatrix(filename):
    
    lines = []
    with open(filename) as file:
        for line in file: 
            line = line.strip() #Striping the file line by line
            lines.append(line)  #storing everything in a list

#Getting the striped lines and spliting them again and adding line by line to a new list 
    records = []
    for i in lines: 
        records.append(i.split(" "))
    
    disdat.showAllData(records)
