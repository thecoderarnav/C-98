def countwordsfromfile():
    fileName = input("ENTER THE FILE NAME")
    numberofwords = 0
    file= open(fileName,"r")
    for line in file:
        words = line.split()
        numberofwords=numberofwords+len(words)
    print("Number Of Words")
    print(numberofwords)

countwordsfromfile()