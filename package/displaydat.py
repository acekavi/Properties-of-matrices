def showAllData(recs):
    global records
    records = recs
    
    print("[Matrix is]\n")

    for i in records:   #Displaying line by line 
        print(*i,sep="  ")
    
    #Converting string elements inside lists to int
    for i in records:
        for s in range(0, len(i)): 
            i[s] = int(i[s])
    
    print("\n")
    matrixSize()
    highestVal()
    lowestVal()
    starDisplay()
    sumVal()
    productVal()
    firstNumber()
    lastNumber()
    oddOrEven()

def matrixSize():
    print("Matrix size is\t\t:",len(records),"x",len(records[1]))

def highestVal():
    highest = 0
    
    for i in records:
        high = max(i)
        if high > highest:
            highest = high
    
    print("Highest Value is\t:",highest)

def lowestVal():
    global lowest
    lowest = 9999
    
    for i in records:
        low = min(i)
        if low < lowest:
            lowest = low
    
    print("Lowest Value is\t\t:",lowest)

def starDisplay():
    star = ""

    for i in range(lowest):
        star += "*"

    print("Star pattern\t\t:",star)

def sumVal():
    total = 0
    
    for i in records:
        total += sum(i)

    print("Addition of values\t:",total)

def productVal():
    product = 1

    for i in records:
        result = 1
        for s in i: 
            result = result * s  
        product = product * result

    print("Product of values\t:",product)

def firstNumber():
    firstnum = records[0][0]

    print("First Number\t\t:",firstnum)

def lastNumber():
    lastnum = records[-1][-1]

    print("Last Number\t\t:",lastnum)
    
def oddOrEven():
    odd = []
    even = []

    for i in records:
        for s in i: 
            if (s % 2) == 1:
                odd.append(s)
            else:
                even.append(s)

    print("Odd values\t\t:",*odd)
    print("Even values\t\t:",*even)
