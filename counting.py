def countingwords():
    fileName = input("ENTER FILE NAME")
    numberofcharacters = 0
    file= open(fileName,"r")
    for line in file:
        data = file.read()
       #words = line.split()
        numberofcharacters = len(data)
    print ("Number of Characters")
    print(numberofcharacters)

countingwords()        


